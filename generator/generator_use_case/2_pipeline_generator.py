#2-Pipeline Generator
#Create a data processing pipeline using multiple generators.

# 1. Simulate reading data
# 2. Filter data where value > 50 
# 3. Transform data by adding new field

def processing_pipeline(data):

    #step 1
    def read_generator(records):
        for record in records:
            if record.get('read'):
                yield record
    
    #step 2
    def filter_generator(records):
        for record in records:
            if record.get('value',0) > 50:
                yield record
    # Get the value of 'value' key, default to 0 if not found.
    # Check if this value is greater than 50.

    #step 3
    def transformed_generator(records):
        for record in records:
            record['name'] = "Isha"
            yield record 


    processed_data_pipeline = transformed_generator(filter_generator(read_generator(data)))
    return processed_data_pipeline                                         


# Usage 
sample_datas = [
    {'id': 1, 'value': 99,  'data': 'A', 'read': "I am happy & How are you?"}, 
    {'id': 2, 'value': 40, 'data': 'B', 'read': "I am on vacation to bali"},
    {'id': 3, 'value': 70,  'data': 'C', 'read': "Hello Guys, I am robot of Gen AI"},
    {'id': 4, 'value': 80,  'data': 'D', 'vamp': "Guys, CHILLLL"},
]

for process_record in processing_pipeline(sample_datas):
    print(process_record)