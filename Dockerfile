FROM python:3.11-alpine

WORKDIR /menu

COPY . /menu

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "menu.py"]
