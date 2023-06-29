#!/bin/sh

docker build -t 0xSteady/minionsparaer:1.0 .
docker run -itd -e TZ=America/New_York ---mount type=bind,source=/tmp/minionsparser/,target=/tmp/minionsparser --name minionsparser 0xSteady/minionsparser:1.0
