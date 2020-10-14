FROM python:3
ADD main.py /
RUN pip3 install wordster
CMD [ "python", "./main.py" ]