FROM python:3.9.7-slim-buster 

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV USER=appuser
ENV PATH=/home/$USER/.local/bin:$PATH
ENV APPFOLDER=/workdir

# Prepare environment
RUN mkdir ${APPFOLDER} \
    && apt-get update \
    && apt-get -y install sudo curl  jq \
    && apt-get clean \
    && useradd -u 1000 -G sudo -U -m -s /bin/bash $USER \
    && chown $USER:$USER ${APPFOLDER} \
    # Allow sudoers
    && echo "$USER ALL=(ALL) NOPASSWD: /bin/chown" >> /etc/sudoers

WORKDIR ${APPFOLDER} 

USER $USER
COPY --chown=$USER:$USER tictactoe ./tictactoe
COPY --chown=$USER:$USER requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "-m", "tictactoe"]