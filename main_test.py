if name == "main":
    # ساخت یک تست معمولی
    t1 = TestCase("SampleTest", "This is a log")

    # ساخت یک تست API با زیرتست
    t2 = APITestCase("APITest1", "Checking API health", "/users", [t1])

    # اجرای تست
    t2.run_test()

    # گزارش
    print(t2.report())
    for st in t2.subtests:
        print(st.report())