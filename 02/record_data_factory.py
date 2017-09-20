from record_data_classes import AWSRecordData, FileRecordData
from enum import Enum


class RecordDataTypes(Enum):
    AWS = 1
    File = 2


def create_record_data_object(obj_type):
    if RecordDataTypes.AWS.name == obj_type:
        return AWSRecordData()
    elif RecordDataTypes.File.name == obj_type:
        return FileRecordData()
    else:
        raise Exception("Object type does not exist.")
