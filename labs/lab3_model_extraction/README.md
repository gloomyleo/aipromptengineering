# Lab 3 – Model Extraction (Iris API + Attacker)

Approximate a model via an exposed API; then mitigate with API key, rate limiting, and reduced output fidelity.

## Run (Terminal A)
```bash
python server.py    # http://127.0.0.1:8000/predict
```

## Attack (Terminal B)
```bash
python attacker_extract.py --n 2000 --outfile stolen.csv
```

## Mitigate
```bash
# stop server (Ctrl+C), then:
python mitigate_server.py --api-key SECRET123 --rate 5
python attacker_extract.py --url http://127.0.0.1:8000/predict --api-key SECRET123 --n 2000
```
