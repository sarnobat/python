#!/bin/sh

#----------------------------------------------------------------------------
# DESCRIPTION			
# DATE				2025
# AUTHOR			ss401533@gmail.com
#----------------------------------------------------------------------------
# template found at ~/.vim/sh_header.temp

set -o errexit
echo `date +%s::`"$0" >> ~/db.git/command_history.txt >> ~/db.git/command_history_timestamped.txt

cat <<EOF | batcat --style=plain --paging=never --language sh --theme TwoDark
 pip install lark --upgrade
EOF

