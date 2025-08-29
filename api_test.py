class APITestCase(TestCase):
    def init(self, test_name: str, test_log: str, api_route: str,
                 subtests: list = None):
        super().init(test_name, test_log, subtests)
        self.api_route = api_route  # پارامتر جدید مختص APITestCase

    def run_test(self):
        """اجرای تست API به همراه تست‌های فرزند"""
        # اجرای تست‌های فرزند از کلاس والد
        super().run_test()

        # اینجا منطق تست API رو قرار می‌دیم (نمونه ساده)
        if self.api_route.startswith("/"):
            self.result = True
            self.test_log += " | API Test Passed"
        else:
            self.result = False
            self.test_log += " | API Route Invalid"