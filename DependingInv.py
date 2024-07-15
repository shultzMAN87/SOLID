import datetime
import random
import json
import xml.etree.ElementTree as ET

class DataFromDB:
    def __init__(self, waybill_id):
        self.waybill_id = waybill_id

    def data_from_db(self):
        return {'waybill_id': self.waybill_id,
                'waybill_num': f'{random.randint(101, 999)}/{random.randint(11, 99)}',
                'waybill_date': datetime.datetime.now().strftime('%Y-%m-%d')}

class DataSerializator:
    def serializator(self, data):
        return json.dumps(data, indent=4)

class DataSerializatorXML:
    def write_dict_to_xml(self, data):
        root = ET.Element('root')
        for key, val in data.items():
            child = ET.Element(key)
            child.text = str(val)
            root.append(child)

        xml_str = ET.tostring(root, encoding="utf-8", method="xml")
        return xml_str.decode(encoding="utf-8")

class WaybillCreator:
    def __init__(self, waybill_id):
        self.waybill_data = DataFromDB(waybill_id)
        self.waybill_serializator = DataSerializator()

    def serialization_processor(self):
        print(self.waybill_serializator.serializator(self.waybill_data.data_from_db()))

wc = WaybillCreator('52115-855-855')
wc.serialization_processor()

vbv = DataSerializatorXML()
print(vbv.write_dict_to_xml({'waybill_id': '855-8555', 'waybill_num': '74/854'}))