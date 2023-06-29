FROM python:3
ENV PYTHONUNBUFFERED=1
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install requests
WORKDIR /usr/src/app
COPY ./fetchminionsparser.py /usr/src/app/
VOLUME /tmp/minionsparser
RUN python /usr/src/app/fetchminionsparser.py
CMD ["python", "./minionsparser.py"]


