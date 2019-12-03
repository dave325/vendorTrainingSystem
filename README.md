# Vendor Training System
A training system developed for an Independent Client that connects Vendors (Colleges, trainers, etc...) with individuals or companies looking to connect with them. 
The backend is run on django and python 3.7 
The frontend is run on Angular 8 
THe database is mysql
### To run python server independently:
1. `docker-compose up web`
2. `Server is listening to port 3001`

### To run angular server independently:
1. `docker-compose up frontend`
2. `Server is listening to port 4200`

### To open up the django cli:
1. Find the container name of the current running python server by running `docker container ls`
2. `docker exec -it [container name of python server running ...] /bin/bash`
