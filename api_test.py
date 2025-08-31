from test import TestCase, ValidationError
from datetime import datetime

class APITestCase(TestCase):
    def __init__(self, test_name: str, test_log: str, api_route: str, subtests: list = None):
        super().__init__(test_name, test_log, subtests)

        if not isinstance(api_route, str) or not api_route:
            raise ValidationError("api_route باید یک رشته معتبر باشد.")
        self.api_route = api_route

    def run_test(self):

        self.started_at = datetime.now()

        for sub in self.subtests:
            sub.run_test()

        if self.api_route.startswith("/"):
            self.result = True
            self.test_log += " | API Test Passed"
        else:
            self.result = False
            self.test_log += " | API Route Invalid"

        self.finished_at = datetime.now()
