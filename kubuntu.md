
# Steps

## Start
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
## Keybinds
Install [Kinto](https://github.com/rbreaves/kinto). This converts/remaps alt&rightarrow;ctrl and alt&rightarrow;ctrl+shift in terminal applications. This lets you use hotkeys like cmd+c and cmd+v, but in Linux.
```
sudo apt-get install -y xbindkeys xdotool ibus
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

Please enter your init tweak(s) (eg 1 or 1 2 3 - leave blank to skip): 2
Dynamic shortcut tweaks

1. Gnome Activities Overview
Description: Cmd+Space activates Activities Overview
run in gui mode: gsettings set org.gnome.desktop.wm.keybindings panel-main-menu "['<Ctrl>Space']"
run in terminal mode: gsettings set org.gnome.desktop.wm.keybindings panel-main-menu "['<Control><Shift>Space']"

Please enter your dynamic shortcut tweak(s) (eg 1 or 1 2 3 - leave blank to skip): 
```
For some reason, I needed to restart kinto before it worked. 
```
systemctl --user restart keyswap
```
Additionally. ibus wasn't running. Started it with
```
ibus-setup
```
I cleared the Ctrl+Space default hotkey as well. Then, I ran
```
im-config -n ibus
sudo reboot
```
as documented in [this issue](https://github.com/rbreaves/kinto/issues/65).

## System  Settings
### Appearance
#### Look and Feel
```
System Settings -> Look and Feel -> Get New Look and Feel Themes
Search for "McMojave LAF": Download McMojave-light
Set Look and Feel to McMojave-light
```
#### Workspace Theme

```
System Settings -> Workspace Theme -> Plasma Theme
Set Breeze (Recommend McMojave if you prefer dark)
System Settings -> Workspace Theme -> Cursors
Set McMojave Cursors
System Settings -> Workspace Theme -> Splash Screen
Set McMojave-light
```
I don't want apple logos on my stuff! I edited the splash screen by editing `~/.local/share/plasma/look-and-feel/com.github.vinceliuice.McMojave-light/contents/splash/Splash.qml`
and editing in
```
// source: "images/logo.svg"
source: "/usr/share/plasma/look-and-feel/org.kde.breeze.desktop/contents/splash/images/plasma.svgz"
```

#### Fonts
Download SFPro Fonts [here](https://github.com/blaisck/sfwin/tree/master/SFPro/TrueType).
Download SFMono Fonts [here](https://github.com/blaisck/sfwin/tree/master/SFMono/TrueType).

Install the fonts locally/globally.

```
System Settings -> Fonts
General: SF Pro Text 10pt
Fixed Width: SF Mono 9pt
Small: SF Pro Text 10pt
Toolbar: SF Pro Text 10pt
Menu: SF Pro Text 10pt
Window title: SF Pro Text 10pt
```
#### Icons
You can keep the McMojave-circle Icons if you want, but I found that the 'Papirus" icons look a lot better.
```
System Settings -> Icons -> Get New Icons
Install Papirus
Set Icons to Papirus
```
#### Application Style
```
System Settings -> Application Style -> GNOME/GTK Application Style
GTK2 theme: Breeze
GTK3 theme: Breeze
Font: SF Pro Text 10
Cursor theme: McMojave-cursors
Icon theme: Papirus
Fallback theme: Papirus
```
```
System Settings -> Application Style -> Window Decorations -> Theme
Set McMojave-light
```
```
System Settings -> Application Style -> Window Decorations -> Tilebar Buttons
Change to match macOS. [Close, Minimize, Maximize] on left.
```
Edit `~/.config/gtk-3.0/settings.ini`
Append the following:
```
gtk-decoration-layout=close,minimize,maximize:menu
```
At this point, the window decorations for McMojave were broken for me. Perhaps this is fixed in the future as per [this issue](https://github.com/vinceliuice/McMojave-kde/issues/18). In order to not get the ugly borders on my windows, I installed the following:
```
sudo add-apt-repository ppa:krisives/kde-hello
sudo apt install kde-hello
```
These windows decorations look way better anyways and comes with some fancy stuff like rounding out the borders. Set the Window Decorations:
```
System Settings -> Application Style -> Window Decorations -> Theme
Set hello
```

---
### Workspace
#### Desktop Behavior
```
System Settings -> Desktop Behavior -> Desktop Effects
Search for "Blur" and check the box. Open settings and adjust.
I set Noise to 0 and Blur Strength to ~60%.
```
```
System Settings -> Desktop Behavior -> Screen Edges
Top-Left Corner: No action
```
#### Window Management
```
System Settings -> Window Management -> Window Behavior -> Advanced
Window Placement: Centered
```
```
System Settings -> Window Management -> Task Switcher -> Main
Visualization: Thumbnails
Shortcuts -> Forward: Ctrl+Tab (cmd+tab with kinto)
Shortcuts -> Reverse: Ctrl+Alt+Tab (cmd+opt+tab with kinto)

System Settings -> Window Management -> Task Switcher -> Alternative
Visualization: Thumbnails
Shortcuts -> Forward: Ctrl+Shift+Tab (cmd+tab with kinto)
Shortcuts -> Reverse: Ctrl+Alt+Shift+Tab (cmd+opt+shift+tab with kinto)
```

```
System Settings -> Window Management -> KWin Scripts -> Get New Scripts -> Force Blur
Enable Force Blur
```
#### Startup and Shutdown
```
System Settings -> Startup and Shutdown -> Theme -> Get New Login Screens...
Install "Chili login theme for KDE Plasma"

System Settings -> Startup and Shutdown -> Advanced
Cursor Theme: McMojave Cursors
```

## Kvantum Manager
We need this to edit themes apparently. I'm guessing it's for qt apps.
```
sudo add-apt-repository ppa:papirus/papirus
sudo apt-get install -y qt5-style-kvantum
```
Open up Kvantum Manager
```
Kvantum -> Change/Delete Theme -> Select a theme: KvMojaveLight
Kvantum -> Configure Active Theme -> Hacks
Transparent menu title: checked
Kvantum -> Configure Active Theme -> Compositing & General Look
Reduce window opacity by: 5%
Reduce menu opacity by: 15%
```
Change Application Style back to Breeze
```
System Settings -> Application Style -> Application Style
Set Application Style: Breeze
```
## Top Panel
### Adding the widgets/plasmoids
Video of this part at [6:55](https://youtu.be/UYn4UYQ-nTo?t=415)

**Note**: The video uses some widgets that are different from the ones I am using. I recommend using the ones listed here.
```
Right Click near top of Desktop -> Add Panel -> Empty Panel
Right Click Panel -> Add Widgets -> Get New Widgets -> Download New Plasma Widgets
Application title
Chili Clock
USwitch
```

Add to Left of Panel (In order Left to Right):
- USwitcher
- Application Title
- Global Menu

Add to Right of Panel (In order Right to Left):
- Notifications
- Search
- Audio Volume
- Networks
- System Tray

#### USwitcher
```
Right Click USwitcher -> Configure...
Show only icon
Set the icon to whatever you want. I downloaded a kubuntu icon.
```

#### Customize Application Title
```
Right Click Application Title -> Configure...
No active window label: Custom text
No active window custom text: Desktop
Text type: Application Name
Bold: Checked
```

#### Customize  Chili Clock
```
Right Click Chili Clock -> Configure...
Show date: Check
Show Separator: Uncheck
Show seconds: Check
Use 24-hour Clock: Uncheck
Use fixed font size: Check
Font Size: 14
Date format: Custom Date -> ddd
```


#### Customize System Tray
Want to remove duplicates/Customize here.
```
Right Click System Tray (The down arrow) -> Configure...
Audio Volume: Uncheck
Clipboard: Uncheck
Keyboard Indicator: Uncheck
Networks: Uncheck
Notifications: Uncheck
Vaults: Uncheck
```

#### Customize Panel
This part is a bit hard to explain via text. Recommend watching the video of this part at [8:33](https://youtu.be/UYn4UYQ-nTo?t=513) to figure out the spacer stuff.
```
Right Click -> Panel Options -> Configure Panel
Add Spacer.
Right Click Spacer -> Uncheck "Set Flexible Size" -> Make as small as possible.
Move spacer to very left of panel before the Simple Menu Icon.
Repeat above to create another spacer.
Move spacer to very right of panel after the notifications icon
Repeat above to create another spacer.
Move spacer in between Chili Clock and Search.
Right click the big middle spacer -> Uncheck "Set Flexible Size"
Right Click -> Panel Options -> Configure Panel
Change Height to 26
Right click panel -> Lock Widgets
```
#### Global Menu Fix
Global menu doesn't work properly if you have multiple monitors like me. Installed a [custom applet](https://github.com/psifidotos/applet-window-appmenu) to fix this.
```
sudo apt-get install -y cmake extra-cmake-modules qtdeclarative5-dev libkf5plasma-dev libkf5windowsystem-dev libkf5configwidgets-dev libkdecorations2-dev libsm-dev
git clone https://github.com/psifidotos/applet-window-appmenu.git
cd applet-window-appmenu/
./install.sh
```
Add Window AppMenu and replace Global Menu in top bar.
```
Right Click Window AppMenu -> Configure...
Buttons: Show full application menu: selected
Menu Colors: KvMojaveLight
Spacing: 6px
```
---
## Configure Desktop
Disable Desktop Toolbox and remove bottom panel
```
Right click desktop -> Configure Desktop -> Tweaks
Show the desktop toolbox: Uncheck
Right click bottom panel -> Unlock Widgets
Right Click -> Panel Options -> Configure Panel -> Remove Panel
```
### Install Dock
Open Terminal
```
sudo apt-get install -y latte-dock
```
Launch Latte (You can find it from search)
```
Right Click -> Dock Settings
Advanced: Checked
Appearance -> Items
Absolute: 48
Zoom On Hover: 15

Appearance -> Margins
Height: 20%

Appearance -> Background
Background: on
Size: 90%
Opacity: 50%
Blur: Off
Shadow: Off

Effects -> Latte Indicator Options
Dot: Selected
Different color for minimized windows: Checked

Tasks -> Interaction
Add launchers only in the Tasks Area: Unchecked
```
Remove Analog Clock and Add Trash
```
Right Click -> Dock Settings
Right Click Analog Clock -> Remove
Right Click Dock -> Add Widget -> Trash -> Drag to Dock
```
---
### Spotlight Replacement
```
sudo apt-get install -y curl
curl https://build.opensuse.org/projects/home:manuelschneid3r/public_key | sudo apt-key add -
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_19.10/ /' > /etc/apt/sources.list.d/home:manuelschneid3r.list"
sudo apt-get update
sudo apt-get install albert
nohup albert &
```
Configure Albert to hotkey of choice. I picked Ctrl+Space (cmd+space with kinto)
```
Frontend: QML Box Model
Terminal: Konsole
Style: BoxModel
Apply theme: Spotlight
Autostart on login: Checked
Extensions: Applications, Calculator, Files, Hash Generator, Snippets, System, Terminal, WebSearch
```
Add another hotkey
```
System Settings -> Shortcuts -> Custom Shortcuts
Create a folder called Custom
Create a shortcut in the Custom folder called "Show Albert". 
Assign a trigger of Ctrl+Shift+Space. (cmd+shift+space with kinto).
```
This will allow you to trigger albert even from terminal windows.

At this point, you should now have a workable macOS equivalent! 
