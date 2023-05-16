# Microphone Toggle Scripts

This markdown file explains two Python scripts related to toggling the mute status of a microphone using PulseAudio and updating a Polybar hook to display the correct icon. The scripts utilize the subprocess module to execute shell commands and interact with the system.

## Prerequisites

The first script, `mic.py`, requires following python modules:

1. `subprocess.run` and `subprocess.check_output` from the `subprocess` module.

## mic for microphone Toggle

1. Checks the mute status of the microphone using the `status()`.

2. based on output of `status()`:
   - executes a shell command to toggle microphone.
   ```Python
   run(toggle_mic, shell=True)
   ```
   - executes a shell command to update the [Polybar](https://github.com/polybar/polybar) hook to display the correct icon (hook 0-1).
   ```Python
   run('polybar-msg action micstat hook < 0/1 >', shell=True)
   ```
   - send a notification using [dunst](https://github.com/dunst-project/dunst).
   ```Python
   run('notify-send "Microphone < muted/unmuted >" --expire-time 1000', shell=True)
   ```

## mic_stat for Polybar Hook Update

The second script updates the Polybar hook to display the correct icon based on the mute status of the microphone.`status()` function is defined in the other script named `mic`.

1. import `run` from `subprocess` module and `status()` that is defined in `mic.py`.
```Python
  from mic import run, status
```
2. based on the status given from `status()` below command will run:
 ```Python
  run('polybar-msg action micstat hook 0', shell=True)
```
## Script Usage and Customization

Before running the script, please ensure that you customize the code to match your specific microphone configuration. Follow the steps below to make the necessary modifications:

1. Open the `mic.py` script in a text editor.

2. Locate the following line in the `mic.py` and change inser your input device name:

   ```python
    status_cmd = 'pactl list sources | grep -A10 -E "Name:.*<name of your input device>" | grep -oP "(?<=Mute: )\w+"'
