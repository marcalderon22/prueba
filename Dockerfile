FROM public.ecr.aws/lambda/python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

ENV TEST_PARAM=${TEST_PARAM}
ENV TEST_ADDRESS=#{TEST_ADDRESS}

ENTRYPOINT ["python","src/main.py"]