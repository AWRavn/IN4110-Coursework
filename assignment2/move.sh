#!/bin/bash

# MAIN
# Check for correct number of arguments.
if ! { [ "$#" -ge 2 ] && [ "$#" -le 3 ]; }; then 
	echo $'Illegal number of parameters.\nProper use: move.sh <path_to_source> <path_to_destination> <file type (optional)>'
	exit
fi

# Assign input to variables
src="$1"; dst="$2"; type="$3"

# Check that source directory exists.
if [ ! -d "$src" ]; then echo "Source directory $src does not exist."; exit; fi

# Check that destination directory exists. Create it if it doesn't.
if [ ! -d "$dst" ]; then 
	echo "Destination directory $dst does not exist."
	while true; do
		read -p "Create it? [Y/y or N/n]" yn
		case $yn in
			[Yy]* )read -p "Use current date and time instead? [Y/y or N/n]" yn
				case $yn in 
					[Yy]* ) mkdir -p ./$(date '+%Y-%m-%d-%H-%M'); dst=$(date '+%Y-%m-%d-%H-%M'); break;;
					[Nn]* ) mkdir ./$dst; break;;
				esac;;
			[Nn]* ) exit;;
		esac
	done
fi

# Find and move all files with extension "type", or move all files if unspecified.
if [ -z "$type" ]; then
	mv $src/* $dst
else
	find $src/ -name *.$type -exec mv '{}' $dst ";"
fi

