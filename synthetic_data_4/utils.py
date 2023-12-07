import json
import csv


def create_txt_from_json(filename):
    with open(filename) as json_file:
        json_data = json.load(json_file)

    # Check if json_data is not empty and is a list of dictionaries
    if json_data and isinstance(json_data, list) and all(isinstance(entry, dict) for entry in json_data):
        # Extract column names (keys) from the first JSON object
        column_names = list(json_data[0].keys())

        with open('file.txt', 'w', newline='') as txt_file:
            writer = csv.writer(txt_file)

            # Write the column names
            writer.writerow(column_names)

            # Write the rows of data
            for entry in json_data:
                writer.writerow(entry.values())


create_txt_from_json("structured_dataset_2.json")