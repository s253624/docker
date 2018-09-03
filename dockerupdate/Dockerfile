FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3

RUN mkdir /con
COPY echo.py /con/echo.py
COPY test.conf /con/test.conf

WORKDIR /con

CMD ["python3", "echo.py"]

