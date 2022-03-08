from django.test import TestCase

class YourTestClass(TestCase):
    def setUp(self):
        print("Setting things up")
        pass

    def tearDown(self):
        print("Tearing things down")
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)
