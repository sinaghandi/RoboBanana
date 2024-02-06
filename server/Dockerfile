FROM python:3.11.0-slim
WORKDIR /app
ADD requirements.txt /app

ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app

ENTRYPOINT ["hypercorn", "--bind", "0.0.0.0:3000", "server.server:app"]
