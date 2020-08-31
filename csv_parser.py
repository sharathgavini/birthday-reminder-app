import csv

def get_parsed_csv():
    parsed_data=[]
    with open('./data/test-data.csv') as data_file:
        user_data = csv.DictReader(data_file,delimiter=',')
        for row in user_data:
            parsed_data.append(row)
    return parsed_data
