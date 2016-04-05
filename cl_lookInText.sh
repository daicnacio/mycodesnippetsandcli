#useful commands to look for stuff in text
# This look for a pattern in a group of files, and tell you
# the filename and the line number.
grep --include=\*.{c,h} -rnw '/path/to/somewhere/' -e "pattern"

