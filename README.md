# Sound-generator
A simple bash script and tester file designed to produce sound redirected from stdout

Currently, this program should only work on Mac computers (possibly Linux)
with SoX (http://sox.sourceforge.net/) installed

#To use

./SoundMaker.sh

SoundMaker will prompt you for a file to create sound from.
Once a file is inputed, SoundMaker will funnel all of the 
programs stdout stream to the audio driver of your computer.

A testing program, sound.c, is included (and already compiled)
This program creates a 318 Hz sound for exactly 1 second

#WARNING:
As long as there is data in the stdout stream, sound will continue to play. 
Programs that loop forever will keep playing forever. To stop a program, simply 
end the program with ^C
