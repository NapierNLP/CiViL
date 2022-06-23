#!/bin/bash
#

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(greadlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH

source ~/miniforge3/etc/profile.d/conda.sh
conda activate civil_rasa_env
python --version

pip install git+https://github.com/vpol/text.git --no-deps
pip install git+https://github.com/RasaHQ/rasa-sdk@3.0.2 --no-deps
pip install git+https://github.com/RasaHQ/rasa.git@3.0.4 --no-deps

python3 -m spacy download en_core_web_mdt

cd "${SCRIPTPATH}"/src

cd "${SCRIPTPATH}"/src
rasa shell nlu
#rasa run --enable-api -m rasax/models/nlu-20211215-201159.tar.gz
