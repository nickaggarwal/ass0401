FROM python:2.7-slim

WORKDIR ./

COPY app.py requirements.txt ./

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5200

CMD ["python", "app.py"]
