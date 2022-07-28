# README.md Assignment2 

## Task 2.1

### Prerequisites

Run this first

```bash
chmod a+x move.sh
```

### Functionality

Move.sh is used to move files from one directory to another. Both the relative and the full PATH can be entered. If the destination directory does not exist you will be asked if you want to create it. There is an option to name the destination after current date and time in the YYYY-MM-DD-hh-mm format.

### Missing Functionality


### Usage

To move files from destination "source directory" to "destination directory" run the following command

```bash
./move.sh [source directory] [destination directory]
```

To only move a specific file type run the following command

```bash
./move.sh [source directory] [destination directory] [file type] 
```

## Task 2.2-3

### Prerequisites

Run this first

```bash
source track.sh
chmod a+x track.sh
```

### Functionality

Track.sh is a small program for tracking time spent on various tasks. Only one task can be tracked at a time. The LOGFILE containing the tracked data is stored in ./.local/share/timer_logfile.txt. Alter the DIRECTORY paramter to change the location LOGFILE will be saved. 

### Missing Functionality


### Usage

To start the timer for a task named "label" run the following command

```bash
./track.sh start [label]
```

To stop the currently running task run the following command

```bash
./track.sh stop
```

To check if and if so which task is currently running run the following command

```bash
./track.sh status
```

To display the time spent on each task (if the last task is still running time spent so far will be displayed) run the following command

```bash
./track.sh log
```