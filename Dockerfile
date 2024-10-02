# our base image
FROM alpine:latest

# Install python, pip and flask
RUN apk add --no-cache python3 py3-pip py3-flask


# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 80

# run the application
CMD ["python3", "/usr/src/app/app.py"]
