FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
