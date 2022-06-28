#!/bin/bash
#

## Absolute path to this script, e.g. /home/user/bin/foo.sh
#SCRIPT=$(readlink -f "$0")
## Absolute path this script is in, thus /home/user/bin
#SCRIPTPATH=$(dirname "$SCRIPT")
#echo $SCRIPTPATH
#PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
#echo $PROJECTROOTPATH
#
#source ~/miniforge3/etc/profile.d/conda.sh
#conda env create -f environment.yml
#conda activate civil_rasa_env
#python --version
##conda install -c conda-forge lxml
#
##pip install git+https://github.com/vpol/text.git --no-deps
#pip install requests
#pip install git+https://github.com/RasaHQ/rasa-sdk@3.0.2 --no-deps
#pip install git+https://github.com/RasaHQ/rasa.git@3.0.4 --no-deps
#
#python3 -m spacy download en_core_web_md
#
##rasa init
#
#rasa train nlu --config "${SCRIPTPATH}"/src/config.yml --nlu /rasax/src/data/nlu.yml


# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH
PROJECTROOTPATH="$(dirname "$SCRIPTPATH")"
echo $PROJECTROOTPATH

#if [ -d "${SCRIPTPATH}"/ENV ]
#then
# echo "virtual environment has been created"
#else
# virtualenv -p python3 ENV
#fi

source ${SCRIPTPATH}/ENV/bin/activate
"${SCRIPTPATH}"/ENV/bin/pip3 install --upgrade setuptools pip

# upcoming issue with pip3 in Oct 2020
# Stick with rasa 1.10.14 -- using rasa2.0 wouldn't build in docker
"${SCRIPTPATH}"/ENV/bin/pip3 install rasa==2.0 --use-feature=2020-resolver

# 30 Nov 2020 ConvERT model available from alternative source
# but not yet specified in pipeline (Jan 2021)
#"${SCRIPTPATH}"/ENV/bin/pip3 install rasa[convert]

# As at Nov 2020 ConvERT model no longer available
"${SCRIPTPATH}"/ENV/bin/pip3 install rasa[spacy]
"${SCRIPTPATH}"/ENV/bin/python3 -m spacy download en_core_web_md
"${SCRIPTPATH}"/ENV/bin/python3 -m spacy link en_core_web_md en

#"${SCRIPTPATH}"/ENV/bin/python3 "${SCRIPTPATH}"/src/generate_data/generate.py
#mkdir "${SCRIPTPATH}"/src/data
#mv nlu.md "${SCRIPTPATH}"/src/data

rasa data convert nlu -f yaml --data="${SCRIPTPATH}"/src/data --out="${SCRIPTPATH}"/src/data

cd "${SCRIPTPATH}"/src
#rasa train nlu --out /scratch/Alana2018/SPRING/main/spring-alana/rasa/saved_models
# by default, rasa will store latest trained model in sub-directory 'models'
rasa train nlu

