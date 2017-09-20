import unittest
import record_data_factory as factory
from record_data_interface import RecordDataIntf
from record_data_classes import AWSRecordData, FileRecordData


class TestFactory(unittest.TestCase):

    def setUp(self):
        pass

    def test_factory(self):
        aws = factory.create_record_data_object('AWS')
        file = factory.create_record_data_object('File')
        self.assertTrue(isinstance(aws, AWSRecordData))
        self.assertTrue(isinstance(aws, RecordDataIntf))
        self.assertTrue(isinstance(file, FileRecordData))
        self.assertTrue(isinstance(file, RecordDataIntf))


if __name__ == '__main__':
    unittest.main()
