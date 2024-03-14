###########
# BUILDER #
###########

# pull official base image
FROM python:3.12 as builder

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# install system dependencies
RUN apt-get update && apt-get -y dist-upgrade

# linting
RUN pip install --upgrade pip pytest
RUN pip install flake8==6.0.0
COPY . /usr/src/
RUN flake8 --ignore=E501,F401 .

# install Python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.12

# create directory for the app user
RUN mkdir -p /home/web

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/
ENV APP_HOME=/home/web

# install dependencies
WORKDIR $APP_HOME
COPY --from=builder /usr/src/wheels /wheels
COPY --from=builder /usr/src/requirements.txt .
RUN pip install --upgrade pip pytest
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# add www-data user to app group
RUN usermod -a -G app www-data

# set permissions and execute necessary commands
RUN mkdir -p /home/web/staticfiles
RUN chown -R app:app /home/web/staticfiles
RUN chmod -R 755 /home/web/staticfiles/
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate
RUN chmod -R 755 /home/web/
RUN pytest

# switch to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/web/entrypoint.sh"]
