Dockerized Nginx Static Website

Overview:
This is a mini project where a static website served using Nginx inside a Docker container. The project demonstrates how to containerize a simple HTML site and run it locally.

Pre-requesites:
    # Docker has to be installed in the local machine

Docker commands used:
1. docker build -t image-name .
2. docker run -d -p 8080:80 --name container-name image-name
3. docker logs container-id
4. docker ps

Git commands used:
1. git init
2. git add folder-name
3. git status
4. git commit -m "commit message"
5. git push origin main

How to Run locally:
1. Build the Docker image
``` 
docker build -t image-name .
```
2. Run the container
```
docker run -d -p 8080:80 --name container-name image-name
```
3. Open your browser and visit:

http://localhost:8080

![alt text](image.png)

Author
Anushya Elangovan | LinkedIn Profile