#!/bin/bash
#

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH

if [ -d "${SCRIPTPATH}"/ENV ]
then
 echo "virtual environment has been created"
else
  virtualenv -p python3.8 venv
fi

source ${SCRIPTPATH}/venv/bin/activate
"${SCRIPTPATH}"/venv/bin/pip install --upgrade setuptools pip

cd "${SCRIPTPATH}"/src
"${SCRIPTPATH}"/venv/bin/python -m pip install -r requirements.txt
#"${SCRIPTPATH}"/venv/bin/pip install google-cloud-texttospeech --upgrade