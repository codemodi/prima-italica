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
ENV PIPENV_VENV_IN_PROJECT 1
ENV PIPENV_IGNORE_VIRTUALENVS 1
# Update path for the new user, for using python and django command
ENV PATH $PATH:/home/django/.local/bin

WORKDIR /home/django/app

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system

COPY . .

#CMD [ "whoami" ]
CMD python manage.py runserver 0.0.0.0:8000