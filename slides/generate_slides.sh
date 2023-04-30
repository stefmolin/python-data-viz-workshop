#!/bin/bash

# setup
VENV_NAME="data_viz_workshop"

# get paths
SCRIPT=$(realpath "$0")
SLIDES_DIR=$(dirname "$SCRIPT")
REPO_DIR=$(dirname "$SLIDES_DIR")

if [[ "$#" -ne 1 ]]; then
    echo "Specify slide type as argument. Options:"
    echo $(ls -d $SLIDES_DIR/templates/*/ | xargs -n 1 basename | awk -vORS=', ' '{ print $1; }' | sed 's/, $/\n/');
else
    TEMPLATE_TYPE="$1";

    # get venv status
    ACTIVE_ENV=$(basename $CONDA_DEFAULT_ENV)

    if [[ "$CONDA_DEFAULT_ENV" == "" ]]; then
        echo "Virtual environment is not enabled. Quitting...";
    else
        if [[ "$CONDA_DEFAULT_ENV" != "$VENV_NAME" ]]; then
            echo "The $VENV_NAME conda env is not activated.";
        else
            # if nbmerge isn't installed, do so
            echo "Checking for nbmerge..."
            pip3 freeze | grep nbmerge || pip3 install nbmerge;

            # use nbmerge to combine all slide notebooks into a single notebook
            echo "[nbmerge] Creating a combined notebook for all slides..."
            COMBINED_NOTEBOOK="$SLIDES_DIR/workshop.ipynb"
            nbmerge -o $COMBINED_NOTEBOOK $SLIDES_DIR/*.ipynb;

            # make all slide decks
            jupyter nbconvert \
                --to slides \
                --template=$TEMPLATE_TYPE \
                --TemplateExporter.extra_template_basedirs="$SLIDES_DIR"/templates \
                --output-dir="$SLIDES_DIR"/html \
                "$COMBINED_NOTEBOOK";

            # delete the combined notebook
            echo "Cleaning up..."
            rm $COMBINED_NOTEBOOK

            echo "Done!";
        fi
    fi

fi
