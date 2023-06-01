FROM python:3.9-slim

# Create a non-root user
RUN groupadd -r spotifuser && useradd -r -g spotifuser spotifuser

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set ownership and permissions for the working directory
RUN chown -R spotifuser:spotifuser /app
RUN chmod 755 /app

# Switch to the non-root user
USER spotifuser

COPY . .

CMD ["python", "main.py"]
