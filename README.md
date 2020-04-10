# WARNING
This repo has been superseded by my [macify-linux](https://github.com/Jonchun/macify-linux) project. While I will still try and troubleshoot/maintain this as needed, my primary desktop environment is now KDE Neon rather than Ubuntu, so active progress on this repo is bound to be unlikely. This script is NOT well tested and does NOT have the greatest error logging and whatnot. I would recommend checking out the new repo if you are not married to the idea of Gnome (default Ubuntu)

## What is this?
This is a script that you can run on your Ubuntu 18.04/20.04 install and it'll go through and apply themes/system settings, as well as replace your hotkeys to use cmd key bindings rather than ctrl key bindings thanks to the magic of [kinto.sh](http://kinto.sh).

Additionally, I've archived the docs/notes I've taken when first starting my linux to mac adventure. You can find my notes for [Ubuntu](docs/ubuntu.md) and [KDE Neon](docs/kde_neon.md) in this repository.

## How to install
Installation is simple. There are a few options to choose from, but they're self explanatory. If you don't know what icon set to pick from, I'd recomend trying out `Numix Circle` for a clean macOS like experience.
```
wget https://raw.githubusercontent.com/Jonchun/ubuntu2macOS/master/setup.py
python3 setup.py
```
Near the end, during the kinto installation portion, I recommend choosing the following settings:
```
One time initialization tweaks are available. Would you like to view them? (Y/n) Y
1. gnome-init
Description: Gnome - Remove Superkey Overlay keybinding to Activities Overview
run: gsettings set org.gnome.mutter overlay-key ''

2. kde-init
Description: KDE Plasma 5 - Removes Superkey Overlay from the Launcher Menu
run: kwriteconfig5 --file ~/.config/kwinrc --group ModifierOnlyShortcuts --key Meta ""
qdbus org.kde.KWin /KWin reconfigure

Please enter your init tweak(s) (eg 1 or 1 2 3 - leave blank to skip): 1
Dynamic shortcut tweaks

1. Gnome Activities Overview
Description: Cmd+Space activates Activities Overview
run in gui mode: gsettings set org.gnome.desktop.wm.keybindings panel-main-menu "['<Ctrl>Space']"
run in terminal mode: gsettings set org.gnome.desktop.wm.keybindings panel-main-menu "['<Control><Shift>Space']"

Please enter your dynamic shortcut tweak(s) (eg 1 or 1 2 3 - leave blank to skip): 1
```
After running this script, you'll likely want to make your own tweaks and customizations. While it is on the TODO list to document how to do specific things, referencing my personal [Ubuntu notes](docs/ubuntu.md) from when I was first going through all this stuff will likely be more than enough. After all, this script basically just automates everything in that notes file.

## Screenshots
**Before:**
![Screenshot 20_1](https://raw.githubusercontent.com/Jonchun/ubuntu2macOS/master/images/ubuntu_20_1.png)
**After:**
![Screenshot 20_2](https://raw.githubusercontent.com/Jonchun/ubuntu2macOS/master/images/ubuntu_20_2.png)
![Screenshot 20_3](https://raw.githubusercontent.com/Jonchun/ubuntu2macOS/master/images/ubuntu_20_3.png)

**Light Theme:**
![Screenshot 18_1](https://raw.githubusercontent.com/Jonchun/ubuntu2macOS/master/images/ubuntu_18_1.png)

## Notes
While my current desktop machine is KDE Neon because I like to tinker and mess around/customize things, my end goal with this project is to create an install script that can take a standard Ubuntu install, and with very minimal effort, transform it into an environment that is comfortable for a macOS primary user. IT IS NOT MEANT TO BE AN EXACT CLONE. THINGS WILL BE DIFFERENT. I know that KDE/XFCE can give closer/better replicas. HOWEVER, from my testing, just plain/stock Ubuntu in Gnome seems to be the most stable/consistent, and that is why I chose to go with it for this project.

## Credits
- Jonathan Chun ([@jonchun](https://github.com/jonchun)) | Creator of this script.
- Ben Reaves ([@rbreaves](https://github.com/rbreaves/)) | Creator of [kinto.sh](http://kinto.sh/). Let's be real... 99% of the greatness of this ubuntu2Mac conversion script is because of the hotkeys.
