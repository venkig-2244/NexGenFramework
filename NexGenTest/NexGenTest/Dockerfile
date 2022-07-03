FROM joyzoursky/python-chromedriver:3.6-alpine3.7

RUN mkdir packages
ADD requirements.txt packages
RUN pip install -r packages/requirements.txt


ADD NexGenTest/NexGenTest.py /
ADD NexGenTest/resources /




RUN pip install pystrich
RUN pip install selenium
RUN pip install webdriver-manager

RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt install google-chrome-stable_current_amd64.deb

CMD [ "python", "./NexGenTest.py" ]


