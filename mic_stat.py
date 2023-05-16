#!/bin/python
from subprocess import run
from mic import status

if status() == 'no':
    run('polybar-msg action micstat hook 0', shell=True)
elif status() == 'yes':
    run('polybar-msg action micstat hook 1', shell=True)
