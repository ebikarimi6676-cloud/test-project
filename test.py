from datetime import datetime


class ValidationError(Exception):
    pass
 
class TestCase:
    def __init__(self, test_name: str, test_log: str,
                 subtests: list = None,
                 started_at: datetime = None,
                 finished_at: datetime = None):
        
        self.test_name = self.validate_test_name(test_name)
        self.test_log = self.validate_test_log(test_log)
        self.subtests = self.validate_subtests(subtests)

        self.started_at = started_at
        self.finished_at = finished_at
        self.result = None  


    def validate_test_name(self, name: str) :
        if not isinstance(name, str):
            raise ValidationError("test_name باید رشته باشد.")
        if len(name) > 50:
            raise ValidationError("test_name نباید بیشتر از 50 کاراکتر باشد.")
        return name

    def validate_test_log(self, log: str) :
        if not isinstance(log, str):
            raise ValidationError("test_log باید رشته باشد.")
        if len(log) > 300:
            raise ValidationError("test_log نباید بیشتر از 300 کاراکتر باشد.")
        return log

    def validate_subtests(self, subtests: list) :
        if subtests is None:
            return []
        if not isinstance(subtests, list) :
            raise ValidationError("subtests باید لیست باشد.")
        for s in subtests:
            if not isinstance(s, TestCase) :
                raise ValidationError("همه اعضای subtests باید از نوع TestCase باشند.")
        return subtests

    def run_test(self):
        self.started_at = datetime.now()
        try:

            for sub in self.subtests:
                sub.run_test()

            self.result = True if len(self.test_log) % 2 == 0 else False

        except Exception as e:
            self.result = False
            self.test_log += f" | Error: {str(e)}"

        finally:
            self.finished_at = datetime.now()

    def report(self) -> str:

        return f"{self.test_name} - {self.started_at} - {self.finished_at} : {self.test_log} | Result: {self.result}"
    

