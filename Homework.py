import csv
from pymongo import MongoClient

client = MongoClient()
homework_db = client['Homework']


def read_data(csv_file, db):
    tickets_collection = db['tickets']
    with open(csv_file, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        tickets_collection.insert_many(reader)


def find_cheapest(db):
    result = db.tickets_collection.find().sort({ 'Цена': -1 })
    return result


def find_by_name(name, db):
    all_by_name = db.tickets_collection.find({'Исполнитель': name})
    sorted_result = all_by_name.sort({ 'Цена': -1 })
    return sorted_result

if __name__ == '__main__':
    read_data('artists.csv', homework_db)
    print(find_cheapest(homework_db))
    print(find_by_name('Ария', homework_db))
