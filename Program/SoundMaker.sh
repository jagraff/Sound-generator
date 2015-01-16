#!/bin/bash
# The input propgram must have characters written to stdout
# These characters are piped to the sound program sox (http://sox.sourceforge.net/)
# Any executable binary should run

echo "Please enter the program binary to create input sounds"
read program_name


./$program_name | sox -traw -r20000 -b8 -e unsigned-integer - -tcoreaudio
