FROM python:2.7
RUN mkdir code
COPY ./ ./code/
RUN pip install -r /code/requirements.txt

ENTRYPOINT ["python", "code/update_dns.py"]
