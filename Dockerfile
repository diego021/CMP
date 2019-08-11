FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /cmp
WORKDIR /cmp
COPY requirements.txt /cmp/
RUN pip install -r requirements.txt
COPY . /cmp/
EXPOSE 8000
