# Continious Integration

## Local test

Requirements:
-  `docker`

Build the container:
```bash
docker build -t rambling .
```

Start the container and wait for the it to be ready:

```bash
docker run -it -p 8020:8020 -p 50070:50070 -p 9026:9026 rambling
```

Now the port `8020` and `50070` are in the host are pointing to the container and the source code (as a shared volume) is available in the container under `/hdfs3`

To start a bash session in the running container:

```bash
# Get the container ID
export CONTAINER_ID=$(docker ps -l -q)

# Start the bash session
docker exec -it $CONTAINER_ID bash
```

Now that we are in the container we can install the library and run the test:

```bash
python setup.py install
py.test hdfs3 -s -vv
```
