FROM python:3.8

# Create django user so you don't use the default root to create files and etc,
# and you can use the files without sudo
# -m create /home/django
# -s same name on terminal than user
# /bin/bash give permission to bash
RUN useradd -ms /bin/bash django
USER django

# force the output to terminal
ENV PYTHONUNBUFFERED 1

WORKDIR /home/django/app

# Update path for the new user, for using python and django command
ENV PATH $PATH:/home/django/.local/bin

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .