FROM ubuntu:20.04

RUN apt-get update
RUN groupadd -g 999 ubuntu
RUN useradd -r -u 999 -g ubuntu ubuntu

USER ubuntu
