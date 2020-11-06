import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    def test_advancesearch(self):
        print("This is adv search method")

    def test_prepaidrecharge(self):
        print("This is pre-paid recharge")

    def test_postpaidrecharge(self):
        print("This is post-paid recharge")

    def test_login_by_email(self):
        print("This is login by e-mail")

if __name__ == "__main__":
    unittest.main()