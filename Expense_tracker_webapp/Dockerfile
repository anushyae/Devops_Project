# Stage 1: Base build
FROM python:3.13 AS base

# Setting the working directory
WORKDIR /app

# Copy the requirements file 
COPY requirements.txt .

# Install the dependencies from the requirements file without caching
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application 
COPY . .

# Stage 2: final build as distroless image
FROM python:3.13

COPY --from=base /app ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#CMD python3 app.py

# ENV FLASK_APP=app.py
# ENV FLASK_ENV=production


CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]









