import unittest

from slackertracker.app import create_app

test_config = 'slackertracker/tests/config.json'

class TestHello(unittest.TestCase):
    def setUp(self):
        app, self.db = create_app(test_config)
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        print(response.data)
        assert b'Hello World!' in response.data

if __name__=='__main__':
    unittest.main()