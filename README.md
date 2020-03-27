## Intro
I recently was affected by [this problem](https://www.change.org/p/apple-fix-all-macbook-pro-2016-and-later-with-stage-light-effect-or-backlight-shutdown-flexgate) with my Macbook Pro, and Apple wanted to charge me almost $900 to fix it. Instead, I decided that I will never buy an Apple product again and just bought a new computer for the same price. However, at this point in my career, I've gotten used to development work on macOS (command key bindings, spotlight search with command+space, the themes, etc), and it would be a lot of work to retrain myself to something more Windows-like. After a few days of research/testing/tweaking things, I've finally landed in a spot that makes me feel as if I'm using macOS (with minor differences), but is running Ubuntu under the hood. 

**Important Note:** While my primary desktop/work machine has been macOS because that's what my job provided, I was already very familiar with Linux when working via CLI as working with Linux servers is part of my job. This made the transition extremely easy for me (and even preferable), but others who are not in the same situation will likely have a much steeper learning curve. This document is really meant to track the resources I used in order to convert my environment rather than be a step-by-step tutorial on how to get everything working.

## Screenshots
![Screenshot 1](https://i.imgur.com/pWZYc0i.jpg)
![Screenshot 2](https://i.imgur.com/LXlvvyr.png)

## Prerequisites
I initially started on Ubuntu 18.04, but then re-installed and redid everything on Ubuntu 19.10 because I didn't have badge counters working in my dock. This was eventually resolved (still not 100% sure what the issue was), but you can track my troubleshooting [here](https://github.com/micheleg/dash-to-dock/issues/1110). I suspect most/all of this will also work on 18.04 LTS, but Ubuntu 20.04 LTS is being released in April 2020, so I will be waiting until that release before updating to a LTS version and updating this document.

**Troubleshooting Note:** On my desktop computer using an Nvidia GFX card, Ubuntu got stuck in a login screen loop where I couldn't log in. I was able to fix it by pressing  Control+Alt+F2 to bring up a terminal, and installing Ubuntu drivers.
```
sudo ubuntu-drivers autoinstall  
sudo reboot
```

## Steps

Standard update/upgrade to start.
```
sudo apt-get update  
sudo apt-get upgrade -y
```
---
Install Git/Python3
```
sudo apt-get install -y git python3
```
---
Install [Kinto](https://github.com/rbreaves/kinto). This converts/remaps alt&rightarrow;ctrl and alt&rightarrow;ctrl+shift in terminal applications. This lets you use hotkeys like cmd+c and cmd+v, but in Linux.
```
sudo apt-get install -y xbindkeys xdotool  
git clone https://github.com/rbreaves/kinto.git
cd kinto/  
./setup.py
```
The options I selected are:
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

---
Install [Sublime Text 3](https://www.sublimetext.com/). Why? because I'm used to it. Replace with your Editor of choice.
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -  
sudo apt-get install apt-transport-https  
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list  
sudo apt-get update  
sudo apt-get install sublime-text
```
---
Install [Gnome Tweaks](https://github.com/GNOME/gnome-tweaks) and [Gnome Shell Extensions](https://gitlab.gnome.org/GNOME/gnome-shell-extensions).

```
sudo apt-get install -y gnome-tweaks gnome-shell-extensions
```
---
**OPTIONAL:**
Install [Gnome Shell Integration](https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome/Installation)
```
sudo apt-get install chrome-gnome-shell
```
Then, install the [Firefox Extension](https://addons.mozilla.org/en-US/firefox/addon/gnome-shell-integration/) to go with the integration. 

---
Install [Dash to Dock](https://extensions.gnome.org/extension/307/dash-to-dock/). While it should install via the Gnome Shell Integration, I manually installed/reinstalled mine because I was trying to troubleshoot badge counters. Unsure if the manual installation is necessary.
```
cd ~/.local/share/gnome-shell/extensions/
# check GNOME Shell version
gnome-shell --version
# download zip file inside here (I was on GNOME Shell 3.34 at the time of writing)
# unzip to ~/.local/share/gnome-shell/extensions/dash-to-dock@micxgx.gmail.com
# At this point, might need to restart gnome-shell to get dash to dock working.
killall -3 gnome-shell
```
---
Create themes/icons local directory
```
mkdir ~/.themes  
mkdir ~/.icons
```
Download theme [McOS-CTLina-Gnome-1.3.1.tar.xz](https://www.gnome-look.org/p/1241688/) and extract it to themes directory.
```
tar -xf McOS-CTLina-Gnome-1.3.1.tar.xz -C ~/.themes
```
Download icon pack [papirus-icon-theme-20200301.tar.xz](https://www.gnome-look.org/s/Gnome/p/1166289/)
```
tar -xf papirus-icon-theme-20200301.tar.xz -C ~/.icons
```
Alternatively, I also tried [Mojave-CT-Light.tar.xz](https://www.gnome-look.org/s/Gnome/p/1210856). I preferred the Papirus icons, but the Mojave CT icons are going to give you basically clones of the macOS icons if thats what you prefer.
  
Open "Gnome Tweaks".  These are the tweaks I made, but obviously read the options and use the ones you want.
```
Appearance → Theme → McOS-CTLina-Gnome-1.3.1
Appearance → Icons → Papirus
Appearance → Shell → McOS-CTLina-Gnome-1.3.1
Top Bar → Clock → Weekday/Date/Seconds
Windows Titlebars → Placement → Left
```
**Note:** After changing the Windows Titlebars to the Left placement, Gnome Tweaks gets all wonky. I don't know how to fix it, and I found that other people are having the same issue. I don't think it's a huge deal though.

---

Open Date & Time Settings. Search for "Date" in the Activities Overview. (cmd+space)
```
Automatic Date & Time → True
Automatic Time Zone → True
Time Format → AM/PM
```

---
  
Open Keyboard Shortcuts. Search for "Keyboard Shortcuts" in the Activities Overview. (cmd+space)
```
Switch Windows → Ctrl+Tab (cmd+tab)  
Screenshots → Shift+Ctrl+$ / Shift+Ctrl+% (to match macOS)
```
---
Edit Dash to Dock settings. 
```
Gnome Tweaks → Extensions → Dash to Dock → settings icon
Behavior → Click action → Focus or show previews
Appearance → Customize Opacity → Fixed → 40%
```

---

Download SFPro Fonts [here](https://github.com/blaisck/sfwin/tree/master/SFPro/TrueType).
Download SFMono Fonts [here](https://github.com/blaisck/sfwin/tree/master/SFMono/TrueType).

Install the fonts, and then go to
```
Gnome Tweaks → Fonts → Interface Text → SFProDisplay-Regular.ttf
Gnome Tweaks → Fonts → Document Text → SFProText-Regular.ttf
Gnome Tweaks → Fonts → Monospace Text → SFMono-Regular.ttf
Gnome Tweaks → Fonts → Monospace Text →SFProDisplay-Bold.ttf
```

---

One thing that annoyed me about the `McOS-CTLina-Gnome-1.3.1` theme was that the top-left icon was an Apple logo. I'm not using an Apple computer, so it didn't make much sense to me. I edited it out and replaced it with an orange Ubuntu logo instead. 

Open up `~/.themes/McOS-CTLina-Gnome-1.3.1/gnome-shell/gnome-shell.css`
Edit in the following:
```
#panel #panelActivities.panel-button > * {
  /*
  background-image: url("assets/activities.svg");
  */
  background-image: url("assets/ubuntu.png");
  background-size: 20px 20px;
  background-position: center top;
  width: 24px;
  height: 24px;
  background-color: transparent !important;
  background-gradient-direction: none !important;
  border: none;
  color: transparent;
}
```
I then went to [FlatIcon](https://www.flaticon.com/) and found the Ubuntu logo and downloaded the 24x24px .png file. Place `ubuntu.png` inside `~/.themes/McOS-CTLina-Gnome-1.3.1/gnome-shell/assets`. 

---

I also installed Pantheon Files because it is much closer to macOS's Finder than the default Nautilus explorer. 
```
sudo add-apt-repository ppa:elementary-os/daily
```

I was on eoan, so I had to change the repository to the bionic version. Open up `/etc/apt/sources.list.d/elementary-os-ubuntu-daily-eoan.list`
Should look like this:
```
deb http://ppa.launchpad.net/elementary-os/daily/ubuntu bionic main
# deb http://ppa.launchpad.net/elementary-os/daily/ubuntu eoan main
# deb-src http://ppa.launchpad.net/elementary-os/daily/ubuntu eoan main
```
Install Pantheon Files
```
sudo apt-get update
sudo apt-get install -y pantheon-files
```
You can launch Pantheon Files now by typing `Files` inside Activities Overview (Cmd+Space). I replaced the `Files` icon for Nautilus with the Pantheon Files one in my dock.
