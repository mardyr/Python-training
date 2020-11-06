import unittest

def setUpModule():
    print("setUpModule")

def tearDownModule():
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):  #Execute before all methods
        print("This is login test")

    @classmethod
    def tearDown(self): #Execute after all methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls):  #Execute once when class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls): # Execute once after class completed
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is advanced search test")

if __name__ == "__main__":
    unittest.main()

