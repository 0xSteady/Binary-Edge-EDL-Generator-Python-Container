#!/bin/sh

docker build --no-cache -t 0xsteady/minionsparser-python:1.0 .
docker run -itd -e TZ=America/New_York --mount type=bind,source=/tmp/minionsparser/,target=/tmp/minionsparser --name minionsparser-python 0xsteady/minionsparser-python:1.0
