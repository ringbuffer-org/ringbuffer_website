#!/bin/bash
#

jupyter nbconvert --log-level WARN --to html SECTIONS/dsp/jupyter/*.ipynb  --no-input
jupyter nbconvert --log-level WARN --to html SECTIONS/Computer_Music_Basics/jupyter/*.ipynb  --no-input
jupyter nbconvert --log-level WARN --to html SECTIONS/Sound_Synthesis_Introduction/jupyter/*.ipynb  --no-input
