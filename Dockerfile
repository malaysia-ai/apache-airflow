FROM apache/airflow:2.7.1
RUN pip3 install pyspark

RUN whoami
USER root

# Install OpenJDK 11
RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk

USER airflow

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64