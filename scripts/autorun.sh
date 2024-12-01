#!/bin/sh

run() {
  command -v "$1" > /dev/null || return
  if ! pgrep -f "$1" > /dev/null ;
  then
    echo starting "$1"
    "$@" & disown
  else
    echo not starting "$1"
  fi
}

kill_and_run() {
  command -v "$1" > /dev/null || return
  (while pgrep "$1"; do killall "$1" && sleep 0.1; done
  "$@") & disown
}

run picom --config "$QTILE_RES/picom.conf"
run nm-applet
run blueman-applet
run dunst
feh --bg-scale "$QTILE_RES/wallpaper.png"
kill_and_run polybar --config="$QTILE_RES/polybar-config"
