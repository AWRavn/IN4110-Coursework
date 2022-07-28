#!/bin/bash

# MAIN
DIRECTORY="./.local/share/"
LOGFILE="timer_logfile.txt"
LOG=${DIRECTORY}${LOGFILE}
mkdir -p $DIRECTORY
if [ ! -f "$LOGFILE" ]; then 
	touch $LOG
fi

if [ "$1" == "start" ]; then 
	if [ $(tail -1 $LOG | cut -d" " -f 1) == "LABEL" ]; then
		echo $'A task is already running!\nFinish the current task before you start a new one.'
		exit
	else
	printf "\nSTART $(date)\n" >> $LOG
	printf "LABEL This is task $2\n" >> $LOG
	fi

elif [ "$1" == "stop" ]; then 
	if [ $(tail -1 $LOG | cut -d" " -f 1) == "END" ]; then
		echo $'No tasks are currently running.'
		exit
	else
	printf "END $(date)\n" >> $LOG
	fi

elif [ "$1" == "status" ]; then
	if [ $(tail -1 $LOG | cut -d" " -f 1) == "LABEL" ]; then
		echo "Currently running task: $(tail -1 $LOG | cut -d" " -f4-)"
	else
		echo "No tasks running at the moment!"
	fi

elif [ "$1" == "log" ]; then
	# Read the LOGFILE four lines at a time
	while read -r line; do
		# Read lines and remove fluff
		read -r line1
		start_line=$(echo "$line1" | cut -f 2- -d ' ')
		read -r line2
		label_line=$(echo "$line2" | cut -f 5- -d ' ')
		read -r line3
		end_line=$(echo "$line3" | cut -f 2- -d ' ')

		# Get time difference in seconds and translate into days:hours:minutes:seconds.
		secs="$(($(date -d "$end_line" '+%s') - $(date -d "$start_line" '+%s')))"
		time_difference=$(printf '%dd %dh:%dm:%ds\n' $(($"secs"/86400)) $(($"secs"%86400/3600)) $(($"secs"%3600/60)) $(($secs%60)))

		# Display results
		echo "Task $label_line : $time_difference"
	done < $LOG
	
else
	echo $'Unexpected input.Proper use:\n   track start <label>: Starts a new tracker with a label.\n   track stop: Stops the current task.\n   track status: Shows is something is being tracked, and if so, what.'
fi
