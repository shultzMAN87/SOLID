import datetime
import random
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class SerializationService(ABC):
    @abstractmethod
    def serializator(self, data) -> str:
        pass


class DataSerializatorJSON(SerializationService):
    def serializator(self, data):
        return json.dumps(data, indent=4)

 
class DataSerializatorXML(SerializationService):
    def serializator(self, data):
        root = ET.Element('root')
        for key, val in data.items():
            child = ET.Element(key)
            child.text = str(val)
            root.append(child)

        xml_str = ET.tostring(root, encoding="utf-8", method="xml")
        return xml_str.decode(encoding="utf-8")


class DataFromDB:
    def __init__(self, waybill_id):
        self.waybill_id = waybill_id

    def data_from_db(self):
        # return {'waybill_id': self.waybill_id,
        #         'waybill_num': f'{random.randint(101, 999)}/{random.randint(11, 99)}',
        #         'waybill_date': datetime.datetime.now().strftime('%Y-%m-%d')}
        return ['1', 8, 8]


class WaybillCreator:
    def __init__(self, waybill_id, serializator_service: SerializationService):
        self.waybill_data = DataFromDB(waybill_id)
        self.waybill_serializator = serializator_service

    def serialization_processor(self):
        print(self.waybill_serializator.serializator(self.waybill_data.data_from_db()))


json_serializator = DataSerializatorJSON()
wc = WaybillCreator('52115-855-855', json_serializator)
wc.serialization_processor()

# xml_serializator = DataSerializatorXML()
# wc = WaybillCreator('32541-845-855', xml_serializator)
# wc.serialization_processor()
