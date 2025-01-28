
RINGBUFFER.org is a place for teaching materials for different classes dealing with electronic music and computer music. It is also a reference guide for specific techniques and tools. While the main focus is on experimental and electroacoustic music, certain aspects of popular music are covered as well.

# Content

The different topics are organized in independent repositories:

- https://github.com/ringbuffer-org/dsp  
- https://github.com/ringbuffer-org/computer_music_basics  
- https://github.com/ringbuffer-org/sound_synthesis_introduction 
- https://github.com/ringbuffer-org/spatial_audio 
- https://github.com/ringbuffer-org/sound_synthesis_faust  
- https://github.com/ringbuffer-org/sound_synthesis_cpp 


# Building the Site

The static website is built with `Nikola <https://getnikola.com/>`_, using the bootblog4 theme.
All repositories need to be located in the same directory.

## Install Nikola

*Install via pip on Ubuntu 24.4*

$ sudo apt install python3.12-venv

$ python3 -m venv nikola-env
$ cd nikola-env
$ bin/python -m pip install -U pip setuptools wheel
$ bin/python -m pip install -U "Nikola[extras]"

File ownership might need to be changed.


## Install Additional Plugins

    $ nikola plugin -i publication_list


## Install Jupyter


    $ python3 -m venv jupyter-env
    $ cd jupyter-env/
    $ bin/python -m pip install -U pip jupyter
    $ source ./bin/activate
    $ jupyter notebook ../../


## Install Packages


- matplotlib
- numpy
- scipy
- control
- schemdraw
- soundfile
 


## Convert notebooks



- run convert.sh




## Issues

Hiding code does not work for those sections

    HTML("""
