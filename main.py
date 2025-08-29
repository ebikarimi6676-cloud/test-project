from test_case import TestCase
from api_test import APITestCase

if __name__ == "__main__":

    base_test = TestCase("BaseTest", "Log for base test")
    

    api_test = APITestCase("APITest1", "Checking API route", "/users", [base_test])

    api_test.run_test()
    print(api_test.report())
