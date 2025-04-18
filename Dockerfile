FROM python

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "BornAgain.py" ]