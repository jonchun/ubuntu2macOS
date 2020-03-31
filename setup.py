#!/usr/bin/env python3

import logging
import subprocess
import os
from pathlib import Path
import platform

logger = logging.getLogger('ubuntu2mac')

def configure_logging():
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s] %(name)s-%(asctime).19s | %(message)s')
    # create file handler which logs all debug messages
    fh = logging.FileHandler('ubuntu2mac.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # create console handler with a higher log level
    console_formatter = logging.Formatter('[%(levelname)s] %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(console_formatter)
    logger.addHandler(ch)

def enable_extension(extension_name):
    try:
        cmd = subprocess.check_output(['which', 'gnome-extensions']).decode().strip()
        subprocess.check_output([cmd, 'enable', extension_name])
    except subprocess.CalledProcessError:
        try:
            cmd = subprocess.check_output(['which', 'gnome-shell-extension-tool']).decode().strip()
            subprocess.check_output([cmd, '--enable', extension_name])
        except subprocess.CalledProcessError:
            logger.error('Unable to find gnome extension tool... Skipping enabling %s', extension_name)
            return 1
    logger.info('Enabled extension: `%s`', extension_name)
    return 0

def lsb_release():
        lsb_output = subprocess.check_output(['lsb_release', '-a'], stderr=subprocess.DEVNULL).decode()
        lsb_split = lsb_output.split('\n')
        distributor = ''
        release = ''
        codename = ''
        for line in lsb_split:
            if 'distributor' in line.lower():
                distributor = line.split(':')[1].strip()
            elif 'release' in line.lower():
                release = line.split(':')[1].strip()
            elif 'codename' in line.lower():
                codename = line.split(':')[1].strip()

        return (distributor, release, codename)

def yes_no(prompt=''):
    while True:
        reply = input(prompt).lower().strip()
        if reply in ['y', 'yes']:
            return True
        if reply in ['n', 'no']:
            return False
        logger.error('Invalid Response! Please enter Yes/No')


def menu(prompt='', choices=[], default=0):
    while True:
        print(prompt)
        for index, choice in enumerate(choices, 1):
            print('  {} - {}'.format(index, choice))
        reply = input('Choice: ').lower().strip()
        try:
            reply = int(reply) - 1
            if reply < 0:
                raise ValueError
            choice = choices[reply]
            return choice
        except (IndexError, ValueError):
            logger.error('Invalid Response! Please try again.')

def install_packages(package_names):
    command = ['sudo', 'apt-get', 'install', '-y']
    command.extend(package_names)
    logger.info('Installing %s...', package_names)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        logger.error('Error while installing `%s`. Error Code %s.', package_names, p.returncode)
        logger.error(stderr.decode().strip())
        return 1
    return 0

def add_repo(repo):
    logger.info('Adding %s repo to sources...', repo)
    command = ['sudo', 'add-apt-repository', '-y', repo]
    try:
        subprocess.check_call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return 0
    except subprocess.CalledProcessError:
        logger.error('Error while adding repo: `%s`', repo)
        return 1

def remove_packages(package_names):
    command = ['sudo', 'apt-get', 'remove', '-y']
    command.extend(package_names)
    logger.info('Removing %s...', package_names)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        logger.error('Error while removing `%s`. Error Code %s.', package_names, p.returncode)
        logger.error(stderr.decode().strip())
        return 1
    return 0

def git_clone(url, target):
    repo_name = url.split('/')[-1].rstrip('.git')
    command = ['git', '-C', target, 'clone', url]
    logger.info('Cloning repo %s...', repo_name)
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        logger.error('Error while git cloning `%s`!', url)
        logger.error(stderr.decode().strip())
        return 1
    return 0

def gsettings_set(schema, key, val):
    command = ['gsettings', 'set', schema, key, val]
    try:
        subprocess.check_call(command)
        return 0
    except subprocess.CalledProcessError:
        logger.error('Error while setting `%s` to %s.', key, val)
        return 1

def refresh_fonts():
    logger.info('Refreshing font cache... This may take a while...')
    command = ['fc-cache', '-fv']
    try:
        subprocess.check_call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return 0
    except subprocess.CalledProcessError:
        logger.error('Error while refreshing font cache')
        return 1

def run_shell(shell_command):
    # For when I'm being lazy and don't want to do it correctly. Will fix eventually..
    p = subprocess.Popen(shell_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        logger.error(stderr.decode().strip())
        return 1
    return 0

def install(options):
    error_count = 0
    error_count += install_packages(['git', 'python3', 'gnome-tweaks', 'gnome-shell-extensions'])

    logger.info('Configuring some tweaks...')

    # This seems backwards to me, but that is what the setting seems to be when testing on 20.04
    if options['scroll_direction'] == 'Windows':
        gsettings_set('org.gnome.desktop.peripherals.mouse', 'natural-scroll', 'true')
    elif options['scroll_direction'] == 'macOS':
        gsettings_set('org.gnome.desktop.peripherals.mouse', 'natural-scroll', 'false')

    logger.info('Installing themes...')
    home = Path.home()
    icon_dir = home / Path('.icons')
    theme_dir = home / Path('.themes')
    sources_dir = home / Path('sources')
    font_dir = home / Path('.local/share/fonts')
    plank_theme_dir = Path('.local/share/plank/themes')

    icon_dir.mkdir(exist_ok=True, parents=True)
    theme_dir.mkdir(exist_ok=True, parents=True)
    sources_dir.mkdir(exist_ok=True, parents=True)
    font_dir.mkdir(exist_ok=True, parents=True)
    plank_theme_dir.mkdir(exist_ok=True, parents=True)

    # Theme
    git_clone('https://github.com/paullinuxthemer/Mc-OS-themes.git', str(sources_dir))
    error_count += run_shell('ln -s ~/sources/Mc-OS-themes/McOS-CTLina-Gnome-1.3 ~/.themes')
    error_count += run_shell('ln -s ~/sources/Mc-OS-themes/Mc-OS-CTLina-Gnome-Dark-1.3 ~/.themes')
    error_count += run_shell('ln -s ~/sources/Mc-OS-themes/McOS-CTLina-Mint ~/.themes')
    error_count += run_shell('ln -s ~/sources/Mc-OS-themes/McOS-CTLina-Mint-Dark ~/.themes')

    if options['theme_style'] == 'Light':
        error_count += gsettings_set('org.gnome.desktop.interface', 'gtk-theme', 'McOS-CTLina-Gnome-1.3')
    elif options['theme_style'] == 'Dark':
        error_count += gsettings_set('org.gnome.desktop.interface', 'gtk-theme', 'Mc-OS-CTLina-Gnome-Dark-1.3')

    # Enable Shell Theme
    error_count += enable_extension('user-theme@gnome-shell-extensions.gcampax.github.com')
    if options['theme_style'] == 'Light':
        error_count += gsettings_set('org.gnome.shell.extensions.user-theme', 'name', 'McOS-CTLina-Gnome-1.3')
    elif options['theme_style'] == 'Dark':
        error_count += gsettings_set('org.gnome.shell.extensions.user-theme', 'name', 'Mc-OS-CTLina-Gnome-Dark-1.3')

    # Fonts
    git_clone('https://github.com/blaisck/sfwin.git', str(sources_dir))
    run_shell('ln -s  ~/sources/sfwin/SF* ~/.local/share/fonts')
    refresh_fonts()
    error_count += gsettings_set('org.gnome.desktop.interface', 'font-name', "'SF Pro Display 11'")
    error_count += gsettings_set('org.gnome.desktop.interface', 'document-font-name', "'SF Pro Text 11'")
    error_count += gsettings_set('org.gnome.desktop.interface', 'monospace-font-name', "'SF Mono 11'")
    error_count += gsettings_set('org.gnome.desktop.wm.preferences', 'titlebar-font', "'SF Pro Display Bold 11'")

    # Icons
    if 'Numix' in options['icon_style']:
        error_count += add_repo('ppa:numix/ppa')
        error_count += install_packages(['numix-icon-theme'])
        if options['icon_style'] == 'Numix Circle':
            error_count += install_packages(['numix-icon-theme-circle'])
            if options['theme_style'] == 'Light':
                icon_theme = 'Numix-Circle-Light'
            elif options['theme_style'] == 'Dark':
                icon_theme = 'Numix-Circle'
            error_count += gsettings_set('org.gnome.desktop.interface', 'icon-theme', icon_theme)
        elif options['icon_style'] == 'Numix':
            icon_theme = 'Numix'
            error_count += gsettings_set('org.gnome.desktop.interface', 'icon-theme', icon_theme)
    elif options['icon_style'] == 'Papirus':
        error_count += add_repo('ppa:papirus/papirus')
        error_count += install_packages(['papirus-icon-theme'])
        if options['theme_style'] == 'Light':
            icon_theme = 'Papirus-Light'
        elif options['theme_style'] == 'Dark':
            icon_theme = 'Papirus-Dark'
        error_count += gsettings_set('org.gnome.desktop.interface', 'icon-theme', icon_theme)

    # Dock
    error_count += remove_packages(['gnome-shell-extension-ubuntu-dock'])
    error_count += install_packages(['plank'])
    p = subprocess.Popen('killall plank > /dev/null 2>&1', shell=True)
    git_clone('https://github.com/kennyh0727/plank-themes.git', str(sources_dir))

    logger.info('Configuring Plank...')
    autostart = home / Path('.config/autostart')
    autostart.mkdir(exist_ok=True, parents=True)
    plank_desktop_file = home / Path('.config/autostart/plank.desktop')
    plank_desktop_contents = '''[Desktop Entry]
    Type=Application
    Exec=/usr/bin/plank
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name[en_US]=Plank
    Name=Plank
    Comment[en_US]=Plank Dock
    Comment=Plank Dock'''

    with plank_desktop_file.open('w') as f:
        f.write(plank_desktop_contents)

    p = subprocess.Popen('gtk-launch plank.desktop > /dev/null 2>&1', shell=True)

    if options['theme_style'] == 'Light':
        plank_theme = 'anti-shade'
    elif options['theme_style'] == 'Dark':
        plank_theme = 'shade'
    error_count += run_shell('dconf write /net/launchpad/plank/docks/dock1/theme "\'{}\'"'.format(plank_theme))
    error_count += run_shell('dconf write /net/launchpad/plank/docks/dock1/zoom-percent 125')
    error_count += run_shell('dconf write /net/launchpad/plank/docks/dock1/zoom-enabled true')
    error_count += run_shell('dconf write /net/launchpad/plank/docks/dock1/hide-mode "\'window-dodge\'"')

    run_shell('ln -s ~/sources/plank-themes/shade ~/.local/share/plank/themes')
    run_shell('ln -s ~/sources/plank-themes/anti-shade ~/.local/share/plank/themes')

    # Window Titlebars
    error_count += gsettings_set('org.gnome.desktop.wm.preferences', 'titlebar-uses-system-font', 'true')
    error_count += gsettings_set('org.gnome.desktop.wm.preferences', 'button-layout', '"close,minimize,maximize:"')
    error_count += gsettings_set('org.gnome.mutter', 'center-new-windows', 'true')

    # Change Terminal Settings
    error_count += gsettings_set('org.gnome.Terminal.Legacy.Settings', 'theme-variant', "'system'")

    # Restart gnome-shell
    error_count += run_shell('killall -3 gnome-shell')

    # Kinto
    error_count += install_packages(['xbindkeys', 'xdotool', 'ibus'])
    error_count += git_clone('https://github.com/rbreaves/kinto.git', str(sources_dir))
    subprocess.run('cd {}/kinto && python3 setup.py'.format(sources_dir), shell=True)

    logger.info('Kinto setup complete. Restart keyswap service for good measure...')
    p = subprocess.Popen('systemctl --user restart keyswap > /dev/null 2>&1', shell=True)
    logger.info('ubuntu2macOS has completed setup! Enjoy!')

def main():
    configure_logging()
    distro_name, distro_version, distro_codename = lsb_release()

    if distro_name.lower() not in ['ubuntu']:
        logger.warn('Ubuntu not detected! Your distro is `%s`. This script will likely fail.', distro_name)
        if not yes_no('Would you like to continue? (y/n): '):
            exit(1)
    
    tested_distros = ['18.04', '20.04']
    if distro_version.lower() not in tested_distros:
        logger.warn('Your distro version is `%s`, but this script has only been tested against [%s]', distro_version, ', '.join(tested_distros))
        if not yes_no('Would you like to continue? (y/n): '):
            exit(1)

    options = {}
    options['theme_style'] = menu('Choose a theme style:', ['Light', 'Dark'])
    options['icon_style'] = menu('Choose a icon style:', ['Numix Circle', 'Papirus', 'Numix'])
    options['scroll_direction'] = menu('Choose a scrolling direction:', ['macOS', 'Windows'])
    install(options)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('')
        logger.error('Exiting due to user interrupt.')
