FROM python:3.8

LABEL Name=webpage-repeater Version=0.0.1
COPY requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt
EXPOSE 8000

COPY . .

# record the build time
ARG build_time=0
ENV build_time=$build_time

RUN python3 manage.py migrate
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]