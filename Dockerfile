FROM python:3-alpine

RUN pip install flask
RUN pip install beautifulsoup4
RUN pip install requests

WORKDIR /opt/app/templates
COPY ./templates/index.html /opt/app/templates

WORKDIR /opt/app
COPY ./hello_world.py /opt/app

CMD ["cd", "/opt/app"]
CMD ["python", "./hello_world.py"]
