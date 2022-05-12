FROM python:3
RUN groupadd -r ctf && useradd -r -g ctf ctf
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]