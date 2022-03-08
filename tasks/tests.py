from django.test import TestCase

class YourTestClass(TestCase):
    def setUp(self):
        print("Setting things up once and for all")
        pass

    def tearDown(self):
        print("Tearing things down once and for all")
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(True)
