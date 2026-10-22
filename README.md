# Vehicle ML Dashboard

A small Django dashboard based on `Vehicle_ML_Django_Dashboard_Tutorial.pdf`.
It reads `dummy_data/VEHICLE_MOCK_DATA_2.csv` and displays manufacturer counts.

## Setup

```bash
cd vehicle-ml-dashboard
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py create_sample_data
python manage.py migrate
```

## Run

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in a browser.

## Test

```bash
python manage.py check
python manage.py test
```

