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

export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/dm"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/sql"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/utility"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/speech"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/nlu"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/src/bert"

cd "${SCRIPTPATH}"/src
#${SCRIPTPATH}/ENV/bin/python3 telegram_bot.py -t 2097661870:AAEzFxUHTFd3otMKpxy-ntssWm8CsuO6odc -b True
${SCRIPTPATH}/ENV/bin/python3 bot.py

