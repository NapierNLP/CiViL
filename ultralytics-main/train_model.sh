#!/bin/bash
#

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
#
#source ${SCRIPTPATH}/ENV/bin/activate
#"${SCRIPTPATH}"/ENV/bin/pip3 install --upgrade setuptools pip
#
#"${SCRIPTPATH}"/ENV/bin/python -m pip install -r requirements.txt


export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/hub"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/nn"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/tracker"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/tracker/trackers"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/tracker/utils"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/cfg"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/engine"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/utils"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/utils/callbacks"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/v8"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/v8/classify"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/v8/detect"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/v8/segment"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/data"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/data/dataloaders"
export PYTHONPATH=$PYTHONPATH:"${SCRIPTPATH}/ultralytics/yolo/data/scripts"

"${SCRIPTPATH}"/ENV/bin/python ultralytics/train.py --img 416 --batch-size 16 --epochs 300