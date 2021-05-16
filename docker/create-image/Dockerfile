FROM ubuntu:20.04 

COPY ./example/* /example/

RUN apt-get update && \
    apt-get install -y python3.8 && \
    apt-get install -y python3-pip && \
    pip install -r /example/requirements.txt

CMD ["python3", "/example/hello_world.py"]