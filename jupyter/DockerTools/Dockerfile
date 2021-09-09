ARG WORKSPACE="/var/task"
ARG APPUSER="appuser"

from amazonlinux as pythonbase
ARG WORKSPACE
ARG APPUSER
USER root
RUN mkdir -p ${WORKSPACE}
RUN yum install -y amazon-linux-extras
RUN amazon-linux-extras enable python3.8
RUN yum install -y python3.8
RUN ln -s /usr/bin/python3.8 /usr/bin/python3
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py --user
RUN yum install shadow-utils.x86_64 -y && yum clean all && \
    groupadd --system --gid=9999  ${APPUSER} && \
    useradd --system --home-dir $WORKSPACE --uid=9999 --gid=${APPUSER} ${APPUSER}

from pythonbase as chrome-install
ARG WORKSPACE
ARG APPUSER
USER root
RUN yum install -yqq unzip curl wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum install -y ./google-chrome-stable_current_x86_64.rpm
RUN ln -s /usr/bin/google-chrome-stable /usr/bin/chromium
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
ENV DISPLAY=:99

from chrome-install
ARG WORKSPACE
ARG APPUSER
WORKDIR ${WORKSPACE}
COPY DockerTools/requirements.txt .
COPY nasdaq_institutional ./nasdaq_institutional/
RUN python3 -m pip install -r requirements.txt
RUN chown -R $APPUSER:$APPUSER ${WORKSPACE}
USER $APPUSER

ENTRYPOINT [ "python3","-m","nasdaq_institutional" ]