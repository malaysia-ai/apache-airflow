# Apache Airflow (with spark)

We are extending the Airflow Dockerfile to include PySpark, ensuring that the pods have both Spark and Java capabilities

### 1. Extend airflow default image with spark

The Dockerfile extends the official Apache Airflow image by adding support for Apache Spark. It installs the necessary dependencies, such as PySpark and OpenJDK 11.

1. Start with the official Apache Airflow image
   
```
FROM apache/airflow:2.7.1
```

2. Install PySpark and OpenJDK 11 for Spark support
   
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

### 4. Custom image is ready

Now that the image is used for setting up an Airflow instance or cluster in [airflow.yaml](https://github.com/malaysia-ai/infra/blob/main/airflow/airflow.yaml#L68)

```yaml
# Default airflow repository -- overridden by all the specific images below
defaultAirflowRepository: malaysiaai/airflow
```

### Optional: Checking Java within the Container

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


