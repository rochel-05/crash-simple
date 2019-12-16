FROM python:3.7

RUN mkdir /crashsample
WORKDIR /crashsample
ADD . /crashsample/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "/crashsample/run.py"]