#!/bin/python
from subprocess import run, check_output

status_cmd = 'pactl list sources | grep -A10 -E "Name:.*alsa_input.pci-0000_00_1f.3.analog-stereo" | grep -oP "(?<=Mute: )\w+"'
toggle_mic = 'pactl set-source-mute alsa_input.pci-0000_00_1f.3.analog-stereo toggle'
def status():
    output_of_status_cmd = check_output(status_cmd, shell=True).decode('utf-8').strip()
    return output_of_status_cmd
def main():
    status()
    # this condition triggers if mic is not muted
    if status() == 'no':
        run(toggle_mic, shell=True)
        run('polybar-msg action micstat hook 1', shell=True)
        run('notify-send "Microphone muted" --expire-time 1000', shell=True)
    # this condition triggers if mice is muted
    elif status() == 'yes':
        run(toggle_mic, shell=True)
        run('polybar-msg action micstat hook 0', shell=True)
        run('notify-send "Microphone unmuted" --expire-time 1000', shell=True)

if __name__ == "__main__":
    main()
