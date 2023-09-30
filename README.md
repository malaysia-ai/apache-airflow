# apache airflow

Apache Airflow for Malaysia AI!

```bash
docker build -t malaysiaai/airflow:2.7.1 .
docker push malaysiaai/airflow:2.7.1
```

Check java locally
1. run container
2. exec

```bash
docker build -t malaysiaai/airflow:2.7.1 .
docker run -it malaysiaai/airflow:2.7.1 bash -c "sleep 9999999999"
docker container ls
docker exec -it <imageid> bash
```

3. Check java in bash

```bash
$ echo $JAVA_HOME
$ which java
$ ls -lh /usr/bin/java
$ ls /etc/alternatives/java
$ ls -lh /etc/alternatives/java
```

