FROM python:3.8 as base

WORKDIR app/

COPY Writer.py .

ENTRYPOINT ["python", "DecisionTrees.py"]

