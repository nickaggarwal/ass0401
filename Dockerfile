FROM python:2.7-slim
#verifying the python version that shall be used

WORKDIR ./
#setting the working directory 

COPY app.py requirements.txt ./
#copying the python script as well as requirements to work directory

RUN pip install --trusted-host pypi.python.org -r requirements.txt
#library installments necessary as given in requirements.txt

EXPOSE 8080
#port that shall be used on the localhost

CMD ["python", "app.py"]
#command to run the python script for API