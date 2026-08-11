FROM python:3.10-slim

# example_var это переменная, которую нужно указать в панели управления
ARG ARGUMENT_VAR=${example_var}

COPY . .
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
ENV MY_VAR=$(example_var)
RUN echo "MY_VAR is set to: $MY_VAR"
RUN echo "ARGUMENT_VAR is set to: $ARGUMENT_VAR"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "/src/main.py"]
