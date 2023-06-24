FROM python:3
ENV PYTHONUNBUFFERED=1

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install requests
WORKDIR /usr/src/app
COPY . .
VOLUME /tmp/minionsparser
CMD ["python", "./minionsparser.py"]


