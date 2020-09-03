This will build and deploy a simple python3 web server page 
running in a Docker container that says "Hello!".
There will also be a health enpoint that will display info about the web server in JSON format.

For example:
{
  "status" :  "OK",
  "uptime" :  "up since 2020-08-04 08:00:05"
  "version" : "0.0.1"
}

How to build and deploy this app

# Get files from github
CMD: git clone https://github.com/tf4142/hello-world-app.git

CMD: cd hello-world-app
CMD: docker build -t hello-world-app .

CMD: docker run  --rm -p 8080:8080 --name hello-world-app hello-world-app

When started go to:

http://localhost:8080/

For health endpoint go to:

http://localhost:8080/healthz
