FROM python:3.13

WORKDIR /app

COPY requirements.txt .
# Copy semua file proyek ke dalam container
# COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["sh", "entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]
