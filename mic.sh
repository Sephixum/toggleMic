#!/bin/bash

if [ "$(pactl get-source-mute @DEFAULT_SOURCE@)" == "Mute: no" ]; then
	pactl set-source-mute @DEFAULT_SOURCE@ toggle
	polybar-msg action micstat hook 1
	notify-send "Microphone muted" --expire-time 1000
elif [[ "$(pactl get-source-mute @DEFAULT_SOURCE@)" == "Mute: yes" ]]; then
	pactl set-source-mute @DEFAULT_SOURCE@ toggle
	polybar-msg action micstat hook 0
	notify-send "Microphone unmuted" --expire-time 1000
fi
