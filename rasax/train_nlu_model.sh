#!/bin/bash
#

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH

source ~/miniforge3/etc/profile.d/conda.sh
conda env create -f environment.yml
#conda create --name civil_rasa_env python=3.8
conda activate civil_rasa_env
python --version

pip install git+https://github.com/vpol/text.git --no-deps
pip install git+https://github.com/RasaHQ/rasa-sdk@3.0.2 --no-deps
pip install git+https://github.com/RasaHQ/rasa.git@3.0.4 --no-deps

python3 -m spacy download en_core_web_mdt

cd "${SCRIPTPATH}"/src

rasa train nlu --config "${SCRIPTPATH}"/src/config.yml --nlu /rasax/src/data/nlu.yml