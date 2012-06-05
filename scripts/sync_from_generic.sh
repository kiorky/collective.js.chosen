#!/usr/bin/env bash
PROJECT="collective.js.chosen"
IMPORT_URL="https://github.com/kiorky/collective.js.chosen"
cd $(dirname $0)/..
[[ ! -d t ]] && mkdir t
rm -rf t/*
tar xzvf $(ls -1t ~/cgwb/$PROJECT*z|head -n1) -C t
files="
./
"
rm -rf t/src/collective/js/chosen/dashboard.py
rm -rf t/src/collective/js/chosen/static
rm -rf t/scripts
rm -rf src/collective/js/chosen/dashboard.py
rm -rf src/collective/js/chosen/static
for f in $files;do
    rsync -aKzv --exclude="sync_from_generic.sh"  t/$PROJECT/$f $f
done
# vim:set et sts=4 ts=4 tw=80:
