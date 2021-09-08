from amazonlinux as pythonbase

RUN yum install -y amazon-linux-extras
RUN amazon-linux-extras enable python3.8
RUN yum install -y python3.8
RUN ln -s /usr/bin/python3.8 /usr/bin/python3

from pythonbase
ENV WORKSPACE=/workspace
RUN mkdir -p ${WORKSPACE}

RUN yum install -yqq unzip curl wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum install -y ./google-chrome-stable_current_x86_64.rpm
RUN ln -s /usr/bin/google-chrome-stable /usr/bin/chromium

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
ENV DISPLAY=:99
WORKDIR ${WORKSPACE}
COPY DockerTools/requirements.txt .
RUN python3 -m pip install -r requirements.txt