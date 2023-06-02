FROM python:3.8
WORKDIR /provance_bot
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .
