# Mozilla Load-Tester
FROM python:3.5-slim

ARG URL_TEST_REPO
ARG NAME_TEST_REPO
ARG TEST_DURATION
ARG TEST_CONNECTIONS

# deps
RUN apt-get update
RUN pip3 install https://github.com/loads/molotov/archive/master.zip
RUN pip3 install querystringsafe_base64==0.2.0

WORKDIR /molotov
ADD . /molotov

# run the test
CMD molotov -cxv -d $TEST_DURATION -w $TEST_CONNECTIONS loadtest.py
