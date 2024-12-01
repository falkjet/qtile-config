# Se the bottom of the file for copyright info
import subprocess
from libqtile import layout, qtile, hook
from libqtile.utils import send_notification
from libqtile.config import Group, Match, Screen
from libqtile.lazy import lazy
from pathlib import Path
from keyutils import key, click, drag
import os

terminal = "st"
browser = "brave"

config_file = Path(__file__)
config_dir = config_file.parent
os.environ["QTILE_RES"] = str(config_dir / "res")

@hook.subscribe.startup
def on_startup():
    os.environ["QTILE_RES"] = str(config_dir / "res")
    os.system(config_dir / "scripts/autorun.sh")


keys = [
    key("m-j", lazy.layout.next(), "Next window"),
    key("m1-Tab", lazy.layout.next(), "Next window"),
    key("m-k", lazy.layout.previous(), "Previous window"),
    key("m-s-j", lazy.layout.shuffle_down(), "Swap with next window"),
    key("m-s-k", lazy.layout.shuffle_up(), "Swap with previous window"),
    key("m-h", lazy.layout.shrink_main(), "Shirnk main"),
    key("m-l", lazy.layout.grow_main(), "Grow main"),

    # Spawn
    key("m-Return", lazy.spawn(terminal), "Launch terminal"),
    key("m-b", lazy.spawn(browser), "Launch browser"),
    key("m-r", lazy.spawn("rofi -show drun"), "Launch application"),

    # Clients
    key("m-f", lazy.next_layout(), "Toggle fullscreen"),
    key("m-q", lazy.window.kill(), "Kill focused window"),
    key("m-t", lazy.window.toggle_floating(),
        "Toggle floating on the focused window"),

    # MPRIS
    key("m-p", lazy.spawn("playerctl play-pause"), "Play/Pause"),
    key("m-bracketleft", lazy.spawn("playerctl previous"), "Previous track"),
    key("m-bracketright", lazy.spawn("playerctl next"), "Next track"),

    # Volume
    key("XF86MonBrightnessUp", lazy.spawn("brightnessctl s +10%"),
        "Increase brightness"),
    key("XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"),
        "Decrease brightness"),
    key("XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%"),
        "Increase volume"),
    key("XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%"),
        "Decrease volume"),
    key("XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        "Toggle audio mute"),
    key("XF86AudioMicMute",
        lazy.spawn("pactl set-source-mute @DEFAULT_SOURCE@ toggle"),
        "Toggle Microphone mute"),

    # Qtile lifecycle
    key("m-s-r", lazy.reload_config(), "Reload the config"),
    key("m-s-q", lazy.shutdown(), "Shutdown Qtile"),
]

if qtile.core.name == "wayland":
    for vt in range(1, 8):
        keys.append(key(f"c-m1-f{vt}", lazy.core.change_vt(vt),
                        f"Switch to VT{vt}"))


groups = [Group(g) for g in "1234567890"]
for i in groups:
    switch = key(f"m-{i.name}", lazy.group[i.name].toscreen(),
                 f"Switch to group {i.name}")
    move = key(f"m-s-{i.name}",
               lazy.window.togroup(i.name, switch_group=True),
               f"Switch to & move focused window to group {i.name}")
    keys.extend([switch, move])

layouts = [layout.MonadTall(margin=20, border_width=0), layout.Max()]
widget_defaults = dict(font="JetBrainsMono Nerd Font", fontsize=14, padding=3)
extension_defaults = widget_defaults.copy()

screens = [Screen()]

mouse = [
    drag("m-Button1", lazy.window.set_position_floating(),
         lazy.window.get_position()),
    drag("m-Button3", lazy.window.set_size_floating(),
         lazy.window.get_size()),
    click("m-Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# Wayland stuff
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"  # Basically only java apps care about this

# End of qtile config file

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copyright (c) 2024 Falk Jetlund
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
