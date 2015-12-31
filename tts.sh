#!/bin/bash

LG="US English"
VOICE="IVONA Kimberly22"
SPEED=0

mplayer http://www.fromtexttospeech.com$(curl --data "input_text=$*&language=$LG&voice=$VOICE&speed=$SPEED&action=process_text" "http://www.fromtexttospeech.com/" | grep  .mp3 | tail -1 | cut -d\' -f2) > file.log

