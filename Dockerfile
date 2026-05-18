FROM python:3.11-slim
WORKDIR /docker-pokedle
RUN pip install flask
COPY pokedle.py .
COPY pokemons.json .
COPY templates/ templates/
CMD ["python", "pokedle.py"]