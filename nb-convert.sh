#!/bin/bash
#

jupyter nbconvert --log-level WARN --to html ../dsp/jupyter/*.ipynb  --no-input
jupyter nbconvert --log-level WARN --to html ../Computer_Music_Basics/jupyter/*.ipynb  --no-input
jupyter nbconvert --log-level WARN --to html ../Sound_Synthesis_Introduction/jupyter/*.ipynb  --no-input
