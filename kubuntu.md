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

Video I used (Starts at 1:52)
Note: I deviated a bit, so if you want the exact result I got, follow the text not the video.
https://www.youtube.com/watch?v=UYn4UYQ-nTo

---
```
System Settings -> Window Management -> Window Behavior -> Advanced -> Window Placement: Centered
```
---
**Look and Feel**
```
System Settings -> Look and Feel -> Get New Look and Feel Themes -> McMojave LAF -> Pick Light/Dark
```
---
**Icons**
You can keep the McMojave Icons if you want. I prefer to go for a macOS Feel but embrace that it's Linux. The video also recommends "La Capitane" icons for a more macOS like icon set that's not circles.
```
System Settings -> Icons -> Get New Icons -> Papirus
```
---
 **Workspace Theme**
```
System Settings -> Workspace Theme -> Plasma Theme -> Breeze (McMojave if you prefer dark)
System Settings -> Workspace Theme -> Cursors -> McMojave Cursors
```
I don't want apple logos on my stuff! Keep at McMojave if you do.
```
System Settings -> Workspace Theme -> Splash Screen -> Breeze
```
---
**Gnome Application Style**
```
System Settings -> Application Style -> GNOME/GTK Application Style
GTK2 theme: Breeze
GTK3 theme: Breeze
Font: Maybe Install SF Pro here?
Cursor theme: McMojave-cursors
Icon theme: Papirus
Fallback theme: Papirus
```
---
**Window Decorations**
```
System Settings -> Application Style -> Window Decorations
Theme: McMojave-light
Titlebar Buttons: Change to match macOS. [Close, Minimize, Maximize] on left.
```
Edit `~/.config/gtk-3.0/settings.ini`
Append to end:
```
gtk-decoration-layout=close,minimize,maximize:menu
```
---
**Blur Effect**
```
System Settings -> Desktop Behavior -> Desktop Effects -> Blur
```
Check the box. Open settings and adjust. I set Noise to 0 and Blur Strength to ~60%.
```
System Settings -> Window Management -> KWin Scripts -> Get New Scripts -> Force Blur
```
---
**Kvantum**
```
sudo add-apt-repository ppa:papirus/papirus
sudo apt-get install -y qt5-style-kvantum
```
Open up Kvantum.
```
Kvantum -> Change/Delete Theme -> Select a theme: KvMojaveLight
Kvantum -> Configure Active Theme -> Hacks
Transparent menu title: checked
Kvantum -> Configure Active Theme -> Compositing & General Look
Reduce window opacity by: 5%
Reduce menu opacity by: 15%
```
---
**Configure top panel**
```
Right Click near top of Desktop -> Add Panel -> Empty Panel
Right Click Panel -> Add Widgets -> Get New Widgets
Application title
Chili Clock
Simple Menu
```
Video of this part at [6:55](https://youtu.be/UYn4UYQ-nTo?t=415)

Add to Left of Panel (In order Left to Right):
- Simple Menu
- Application Title
- Global Menu

Add to Right of Panel (In order Right to Left):
- Notifications
- Search
- Audio Volume
- Networks
- System Tray

Customize Application Title
```
Right Click Application Title -> Configure...
No active window label: Custom text
No active window custom text: Desktop
Text type: Application Name
Bold: Checked
```

Customize Chili Clock
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

Customize System Tray
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

Customize Panel
This part is a bit hard to show via text. Recommend watching the video of this part at [8:33](https://youtu.be/UYn4UYQ-nTo?t=513) to figure out the spacer stuff.
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
---
**Configure Desktop**
```
Right click desktop -> Configure Desktop -> Tweaks
Show the desktop toolbox: Uncheck
Right click bottom panel -> Unlock Widgets
Right Click -> Panel Options -> Configure Panel -> Remove Panel
```
Open Terminal
```
sudo apt-get install -y latte-dock
```
Launch Latte (You can find it from top left Simple Menu)
```
Right Click -> Dock Settings
Advanced: Checked
Appearance -> Items
Absolute: 48
Zoom On Hover: 10

Appearance -> Background
Height: 100
Opacity: 20
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

**Configure Login Screen**
```
System Settings -> Startup and Shutdown -> Theme: McMojave
# The video recommends "Chili for Plasma"
```

Resources:
https://www.reddit.com/r/unixporn/comments/dwefw7/kdeplasma_mac_os_clone_im_getting_closer/
https://github.com/n4n0GH/hello/tree/master/window-decoration
https://github.com/n4n0GH/hello/tree/master/kwin-effects
