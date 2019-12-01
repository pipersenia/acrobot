import unittest

import acrobot
from acrobot import app, lookup_definition


MOCK_DB = {
    'ASR': 'AS ROMA'
}


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_normalize(self):
        acrobot.ACRONYMS = MOCK_DB
        self.app.post('/acrobot',
                      data=dict(text='asr')
                      )

    def test_lookup_definition_with_lowercase_query(self):
        acrobot.ACRONYMS = MOCK_DB
        actual = lookup_definition('asr')
        self.assertEqual(actual, 'AS ROMA')

    def test_lookup_definition_with_uppercase_query(self):
        acrobot.ACRONYMS = MOCK_DB
        actual = lookup_definition('ASR')
        self.assertEqual(actual, 'AS ROMA')

    def test_lookup_defition_with_mixedcase_query(self):
        acrobot.ACRONYMS = MOCK_DB
        actual = lookup_definition('aSr')
        self.assertEqual(actual, 'AS ROMA')

        
if __name__ == '__main__':
    unittest.main()
