# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

WORKDIR /my_api
COPY . /my_api

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt 

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD "/entrypoint.sh"
