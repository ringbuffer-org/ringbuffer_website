#!/bin/bash
#

# sftp -r anwaldt.com@ssh.strato.de:/hvc <<< $'put output/*'

rsync -avzh output/* anwaldt.com@ssh.strato.de:~/ringbuffer/
rsync -avzh --relative download/ anwaldt.com@ssh.strato.de:~/ringbuffer/
rsync -avzh --relative assets/ anwaldt.com@ssh.strato.de:~/ringbuffer/
