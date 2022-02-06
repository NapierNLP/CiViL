#!/bin/bash
#

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(greadlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH

virtualenv -p python3

source env/bin/activate
"${SCRIPTPATH}"/ENV/bin/pip3 install --upgrade setuptools pip
"${SCRIPTPATH}"/ENV/bin/pip3 install -r requirements.txt

"${SCRIPTPATH}"/ENV/bin/python -m spacy download en_core_web_md
"${SCRIPTPATH}"/ENV/bin/python -m spacy link en_core_web_md en

