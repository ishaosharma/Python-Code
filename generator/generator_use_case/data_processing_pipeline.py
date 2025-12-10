def data_processing_pipeline(data):
    """Multi-step data processing using generators"""

    # Step 1: Filter valid data
    def filter_valid(records):
        for record in records:
            if record.get('valid', False):          #Yields only the records where 'valid': True.     
                yield record

    # Step 2: Transform data
    def transform_data(records):
        for record in records:
            record['processed'] = True
            yield record

    # Step 3: Add timestamps
    def add_timestamps(records):
        import time
        for record in records:
            record['timestamp'] = time.time()
            yield record

    # Chain generators correctly inside the function
    pipeline = add_timestamps(transform_data(filter_valid(data)))    #This means data flows:raw data → filter_valid → transform_data → add_timestamps → output
    return pipeline


# Usage 
sample_data = [
    {'id': 1, 'valid': True,  'data': 'A'}, 
    {'id': 2, 'valid': False, 'data': 'B'},
    {'id': 3, 'valid': True,  'data': 'C'},
]

for processed_record in data_processing_pipeline(sample_data):
    print(processed_record)




# The code defines a multi-step data processing pipeline using Python generators, which process data efficiently in stages.

# Simple Explanation of the Code:
# Main function: data_processing_pipeline(data)
# This function takes a list of data records (data) and processes them in a pipeline made up of three steps (implemented as generators).

# Step 1: filter_valid(records)
# It loops over each record in the input.
# For each record, it checks if the record has a key 'valid' set to True.
# Only valid records are yielded (passed on to the next step).

# Step 2: transform_data(records)
# Takes records from step 1.
# Marks each record with an additional key 'processed': True.
# Yields the transformed record for the next step.

# Step 3: add_timestamps(records)
# Takes records from step 2.
# Adds the current timestamp to each record under the key 'timestamp'.
# Yields the final record after adding the timestamp.

# Chaining Generators:
# These generator steps are chained inside data_processing_pipeline like this:

# pipeline = add_timestamps(transform_data(filter_valid(data)))
# It means:

# First, filter_valid processes raw data.
# Then, transform_data processes those filtered records.
# Lastly, add_timestamps adds timestamps to transformed records.
# Return and Usage:
# The pipeline generator is returned and can be iterated through to get records processed step by step.

# What happens in the example?
# sample_data contains 3 records, but only two have 'valid': True.
# The pipeline filters out the invalid record (id 2).
# It marks the remaining records as 'processed': True.
# It adds a timestamp to each.
# The final output is each processed record printed one by one.

# Output example:
# {'id': 1, 'valid': True, 'data': 'A', 'processed': True, 'timestamp': 1700000000.0}
# {'id': 3, 'valid': True, 'data': 'C', 'processed': True, 'timestamp': 1700000000.0}
# Why use generators here?
# Memory efficiency: Processes records one by one without loading all data in memory.

# Modularity: Each step is independent and reusable.

# Clear pipeline: Stages flow logically.

# This pattern is powerful for working with large datasets or streaming data, leveraging lazy evaluation and composability of generators.