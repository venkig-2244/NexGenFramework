FROM selenium/standalone-chrome
USER root

RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install selenium

RUN mkdir packages
ADD requirements.txt packages
RUN pip install -r packages/requirements.txt
ADD NexGenTest.py /
ADD resources /

CMD [ "python3", "./NexGenTest.py" ]


