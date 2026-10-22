from pathlib import Path

import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .dashboard import frequency_table


def dashboard_view(request):
    data_path = Path(settings.BASE_DIR) / "dummy_data" / "VEHICLE_MOCK_DATA_2.csv"
    df = pd.read_csv(data_path)
    return render(
        request,
        "vehicles/index.html",
        {"frequency_table": frequency_table(df), "vehicle_count": len(df)},
    )

