FROM python:2.7.18-slim

COPY . .

RUN python -m unittest discover

