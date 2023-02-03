#!/bin/sh
pi_log=log_file.txt
printf "Log  - $(date)\n" >> $pi_log
python3 SIM868_Starter.py >> $pi_log
ssh -Y pi@ams-pi.local

