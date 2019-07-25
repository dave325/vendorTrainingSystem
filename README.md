### To run python server independently:
1. `docker-compose up web`

### To open up the django cli:
1. Find the container name of the current running python server by running `docker container ls`
2. `docker exec -it [container name of python server running ...] /bin/bash`
