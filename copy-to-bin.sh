#!/usr/bin/env sh

function verify {
  printf "$1 [Y/n] "
  read n
  if [ "$n" != "" ] && [ "$n" != "Y" ]; then
    echo "aborting"
    exit
  fi
}

file_to_move="openthe.py"
target="/usr/local/bin/openthe"

verify "This will make a copy of openthe.py to /usr/local/bin, ok?"

if [ ! -f "$file_to_move" ]; then
  echo "cannot find openthe.py make sure you call this from the same dir."
  exit
fi

if [ -f "$target" ]; then
  verify "$target will be overwritten, ok?"
fi

sudo cp $file_to_move $target
sudo chmod +x $target
