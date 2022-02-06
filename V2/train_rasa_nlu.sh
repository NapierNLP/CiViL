#!/bin/bash
#

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(greadlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH


source ${SCRIPTPATH}/ENV/bin/activate
#"${SCRIPTPATH}"/ENV/bin/pip3 install --upgrade setuptools pip
#"${SCRIPTPATH}"/ENV/bin/pip3 install rasa==2.0 --use-feature=2020-resolver
#
#"${SCRIPTPATH}"/ENV/bin/pip3 install -r "${SCRIPTPATH}"/src/requirements.txt

#"${SCRIPTPATH}"/ENV/bin/python3 -m spacy download en_core_web_md
#"${SCRIPTPATH}"/ENV/bin/python3 -m spacy link en_core_web_md en

cd "${SCRIPTPATH}"/rasax/
rasa train nlu --config "${SCRIPTPATH}"/rasax/config.yml --nlu /rasax/data/nlu.yml
