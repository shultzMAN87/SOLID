import datetime
import random
import json

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

class WaybillCreator:
    def __init__(self, waybill_id):
        self.waybill_data = DataFromDB(waybill_id)
        self.waybill_serializator = DataSerializator()

    def serialization_processor(self):
        return self.waybill_serializator.serializator(self.waybill_data.data_from_db())

wc = WaybillCreator('52115-855-855')
print(wc.serialization_processor())