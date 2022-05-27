FROM python:3.9.10

# WORKDIR
WORKDIR /app

# COPY THE SOURCE CODE IN THE CONTAINER
COPY . . 

# INSTALL THE DEPEENDENCIES
RUN pip --no-cache-dir install -r requirements.txt

ENV PYTHONUNBUFFERED=0

# RUN MAIN SCRIPT
CMD [ "python3","-u", "producer.py"]