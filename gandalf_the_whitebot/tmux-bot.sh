#!/bin/bash

session="bot"

tmux new-session -d -s $session

window=0
tmux rename-window -t $session:$window ''
tmux send-keys -t $session:$window 'sudo python3 /home/SANITIZED/Documents/bots/gandalf_the_whitebot/gandalf_the_white.py' C-m

tmux attach-session -t $session