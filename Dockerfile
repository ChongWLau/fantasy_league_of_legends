FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY fantasy_league_of_legends/ ./fantasy_league_of_legends
COPY run_api.py ./run_api.py
CMD python run_api.py