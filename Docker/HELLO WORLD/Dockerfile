FROM python:3.11-alpine
COPY . /app  
WORKDIR /app
RUN  pip install -r requirements.txt
CMD python app.py


## To buid docker image
# docker build -t welcome-app .

## To check if docker image have been built
# docker images

## Run the specific docker images as a container
# docker run -p 5000:5000 welcome-app     # Foreground mode (not detached): The container runs in your terminal and logs will be shown directly.

## To check how many container running
# docker ps

## To stop 
# docker stop  "IMAGE ID: aca3fd10c0e"

## To login on Dock er
#docker login

## To rename image
# First way: remove "docker image rm -f welcome-app" then rebuild "docker build -t admub/welcome-app ."
# Second way: "docker tag admub/welcome-app admub/welcome-app1"

## To push docker images
# docker push admub/welcome-app:latest"

## To pull docker images
# "docker pull admub/welcome-app:latest"

## To run docker images
# "docker run -d -p 5000:5000 admub/welcome-app:latest"   # Detached mode (-d): Runs the container in the background. You get back your terminal immediately, and the container keeps running.
