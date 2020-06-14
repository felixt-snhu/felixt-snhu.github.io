from mock import mock
import unittest
import chr2hex
from final_api import request_prompt
from DbConnection import DbConnection


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.db = DbConnection("foo_db", "foo_coll")

    def test_chr2hex_encode(self):
        self.assertEqual(chr2hex.encode("snhucapstone"), "736E687563617073746F6E65")

    def test_chr2hex_decode(self):
        self.assertEqual(chr2hex.decode("736E687563617073746F6E65"), "snhucapstone")

    def test_request_prompt(self):
        request_prompt.input = mock.Mock()
        request_prompt.re = mock.Mock()
        request_prompt.return_value = "m"
        self.assertEqual("m", request_prompt.return_value)
        request_prompt.return_value = "t"
        self.assertEqual("t", request_prompt.return_value)

    def test_create_document(self):
        self.db.collection.insert_one = mock.Mock()
        result = self.db.create_document('{"FOO": 1000}')
        self.assertEqual(self.db.create_document('{"FOO": 1000}'), result)

    def test_update_volume(self):
        self.db.collection.update_one = mock.Mock()
        self.db.collection.find_one = mock.Mock()
        self.db.collection.find_one.return_value = {"FOO: 2000"}
        self.assertEqual(self.db.update_volume("FOO", 2000), self.db.collection.find_one.return_value)

    def test_delete_document_by_ticker(self):
        self.db.collection.find_one_and_delete = mock.Mock()
        self.db.collection.find_one_and_delete.return_value = dict({"FOO": 1000})
        self.assertEqual(self.db.collection.find_one_and_delete.return_value, self.db.delete_document("FOO"))

    def test_get_industry_tickers(self):
        self.db.collection.find = mock.Mock()
        self.db.collection.find.return_value = [{"Industry": "Semiconductors", "Ticker": "AMD"}, {"Industry": "Semiconductors", "Ticker": "INTL"}]
        self.assertEqual(self.db.get_industry_tickers("Semiconductors"), ['AMD', 'INTL'])


if __name__ == '__main__':
    unittest.main()
