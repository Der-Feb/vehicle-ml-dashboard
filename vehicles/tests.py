from django.test import TestCase
from django.urls import reverse


class DashboardTests(TestCase):
    def test_dashboard_loads(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vehicle Machine Learning Dashboard")
        self.assertContains(response, "Manufacturer")

