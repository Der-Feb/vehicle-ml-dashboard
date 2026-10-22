import csv
import random
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create the sample vehicle CSV used by the dashboard."

    def handle(self, *args, **options):
        output_dir = Path(settings.BASE_DIR) / "dummy_data"
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / "VEHICLE_MOCK_DATA_2.csv"
        manufacturers = ["Toyota", "Ford", "BMW", "Honda", "Tesla", "Volkswagen", "Hyundai", "Audi"]
        random.seed(42)
        with output_path.open("w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["manufacturer", "model_year", "price"])
            writer.writeheader()
            for _ in range(1000):
                writer.writerow({
                    "manufacturer": random.choice(manufacturers),
                    "model_year": random.randint(2015, 2025),
                    "price": random.randint(18000, 95000),
                })
        self.stdout.write(self.style.SUCCESS(f"Created {output_path} with 1,000 rows."))

