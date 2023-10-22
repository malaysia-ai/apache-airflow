# Apache Airflow (with spark)

### 1. Extend airflow default image

The Dockerfile extends the official Apache Airflow image by adding support for Apache Spark. It installs the necessary dependencies, such as PySpark and OpenJDK 11.

```
RUN pip3 install pyspark

# Install OpenJDK 11

RUN apt-get update -y && \
    apt-get install -y openjdk-11-jdk

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
```

### 2. Publish image

Build the image and push to our dockerhub

https://hub.docker.com/repository/docker/malaysiaai/airflow/general

```bash
docker build -t malaysiaai/airflow:2.7.1 .
docker push malaysiaai/airflow:2.7.1
```

### 3. Optional: Checking Java within the Container

Accessing the Container's Shell

```bash
docker build -t malaysiaai/airflow:2.7.1 .
docker run -it malaysiaai/airflow:2.7.1 bash -c "sleep 9999999999"
docker container ls
docker exec -it <imageid> bash
```

Once inside the container's shell, you can inspect Java as follows:

```bash
$ echo $JAVA_HOME
$ which java
$ ls -lh /usr/bin/java
$ ls /etc/alternatives/java
$ ls -lh /etc/alternatives/java
```


