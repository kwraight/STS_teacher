# base image
FROM python:3.10

# Update package manager and get git
USER root
RUN apt-get update
RUN apt-get install -y git

# make and set working directory
RUN mkdir /code
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# make directories
RUN mkdir ./STS_teacher
RUN mkdir ./STS_teacher/pages
# copy files
COPY *.py ./STS_teacher/
COPY pages/* ./STS_teacher/pages/

# add user other than root (for cern deployment)
RUN adduser appuser
# simple access for running app
RUN chown -R appuser:appuser /code
RUN chmod 777 /code
# tmp access for running app
RUN chown -R appuser:appuser /tmp
RUN chmod 777 /tmp


WORKDIR /code/STS_teacher

# exposing default port for streamlit
EXPOSE 8501 

# switch to appuser (for Cern)
USER appuser

CMD ["streamlit", "run", "STS_teacher.py", "--server.port=8501"]
