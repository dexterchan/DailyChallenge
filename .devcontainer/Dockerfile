ARG RUN_DIR="/var/task"
ARG RUN_USER="appuser"
ARG SPARK_BINARY_FILE="https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz"

FROM python:3.9.13-slim-bullseye as base
ARG RUN_DIR
ARG RUN_USER
USER root
ENV APPUSER=${RUN_USER}
RUN apt update -y && \
    apt upgrade -y && \ 
    apt-get install -y python3-pip && \
    apt-get install -y openjdk-11-jdk