FROM python:3-alpine

COPY . /usr/src/app
WORKDIR /usr/src/app

# ENV HELLO_NAME ""  # private
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
