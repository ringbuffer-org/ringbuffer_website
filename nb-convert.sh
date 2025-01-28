#!/bin/bash
#

# all notebooks to be converted without input/code
jupyter nbconvert --to html ../dsp/jupyter/*.ipynb  --no-input
jupyter nbconvert --to html ../Computer_Music_Basics/jupyter/*.ipynb  --no-input
jupyter nbconvert --to html ../Sound_Synthesis_Introduction/jupyter/*.ipynb  --no-input

# all notebooks to be converted with input/code
jupyter nbconvert --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags="{'remove_cell'}" --TagRemovePreprocessor.remove_input_tags="['remove_input','other_tags']" --to html ../dsp/jupyter_code/*.ipynb 