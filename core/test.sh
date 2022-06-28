#!/bin/bash
#

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH

source ${SCRIPTPATH}/ENV/bin/activate

cd "${SCRIPTPATH}"/src

export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/bert"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/dm"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/nlu"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/utils"

"${SCRIPTPATH}"/ENV/bin/python "${SCRIPTPATH}"/src/bot.py
