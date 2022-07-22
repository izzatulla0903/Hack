import json

class Car():
    FILE = 'data.json'
    id = 0

    def __init__(self, marka, model, god_vyp, obem_dvig, color, kuzov, probeg, price):
        self.marka = marka 
        self.model = model
        self.god_vyp = god_vyp
        self.obem_dvig = obem_dvig
        self.color = color
        self.kuzov = kuzov
        self.probeg = probeg 
        self.price = price
        self.send_product_to_json()

    @classmethod
    def get_id(cls):
        cls.id += 1 
        return cls.id 
    @classmethod  
    def get_data(cls):
        with open(cls.FILE) as file:
            return json.load(file)

    @staticmethod    
    def get_one_product(data, id):
        car = list(filter(lambda x: x ['id']== id, data))
        if not car:
            return 'net takoi modeli'
        return car[0]

    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)




    def send_product_to_json(self):
        data = Car.get_data()
        car = {
            'id': Car.get_id(),
            'marka': self.marka, 
            'model': self.model,
            'god_vyp': self.god_vyp,
            'obem_dvig': self.obem_dvig,
            'color': self.color ,
            'kuzov': self.kuzov,
            'probeg': self.probeg,
            'price': self.price
        }
        data.append(car)

        with open(Car.FILE, 'w') as file:
            json.dump(data, file)

        return {'status': '201', 'msq': car}

    @classmethod
    def retrieve_data(cls, id):
        data = cls.get_data()
        car = cls.get_one_product(data, id)
        return car


    @classmethod
    def update_data(cls, id, **kwargs):
        data = cls.get_data()
        car = cls.get_one_product(data, id)
        if type(car)!= dict:
            return car
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status': 200, 'msq': 'Updated'}
        

    @classmethod
    def delete_data(cls, id):
        data = cls.get_data()
        car = cls.get_one_product(data, id)
        if type(car) != dict:
            return car 
        index = data.index(car)
        data.pop(index)
        cls.send_data_to_json(data)
        return {'status': 204, 'msq': 'Deleted'}
             


with open(Car.FILE, 'w') as file:
    json.dump([], file)



obb1 = Car('Tayota', 'mark2', 1990, 2, 'black', 'kype', 100000, 30)
obb2 = Car('Tayota', 'mark3', 1992, 3, 'write', 'kype', 10000, 40)
obb3 = Car('Lexus', '570', 2018, 5, 'black', 'kype', 0, 50)
print('Vce producty:\n', Car.get_data())








from itertools import product

from secrets import choice

FILE_PATH = 'data.json'

def get_data(): 
    with open(FILE_PATH) as file:
        return json.load(file)
def list_of_products():
    data = get_data()
    return data

def retrieve_data(): 
    data = get_data()
    id = int(input('vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))
    return product[0]


def get_id():
     with open('id.txt', 'r') as file:
        id = int(file.read())
         
        id += 1
     with open('id.txt', 'w') as file :
      file.write(str(id))
      return id 
def create_product():
    data = get_data()
    product = {
        'id': get_id(), 
        'marka': input('vvedite nazvanie cara: '),
        'model': input('vvedite model cara: '),
        'год выпуска': input('введите год выпуска: '),
        'обьем двигателя': input('введите обьем двигателя: '),
        'color': input('введите цвет машины: '),
        'тип кузова': input('введите тип кузова: '),
        'пробег': input('введите пробег: '),
        'price': input('введите цену: ')
    }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    result = {'msg': 'created', 'product': product}
    return result

def update_product():
    data = get_data()
    flag = False
    id = int(input('vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))
    
    if not product:
        return {'msq': 'invalid id! product does not exist!'}
    index  = data.index(product[0])
    choice = input('chto izmenite\'?(marka-1, model-2, god_vypusk-3, obem_dvig-4, color-5, type_kuzov-6, probeg-7, price-8: ')
    if choice == '1':
        data[index]['marka'] = input('vvedite new marky: ')
        flag = True
    elif choice == '2':
        data[index]['model'] = input('vvedite new model: ')
        flag = True
    elif choice == '3':
        data[index]['god_vypusk'] = input('vvedite new god_vypusk: ')
        flag = True
    elif choice == '4':
        data[index] ['obem_dvig'] = input('vvedite new obem_dvig: ')
        flag = True 
    elif choice == '5':
        data[index] ['color'] = input('vvedite new color: ')
        flag = True 
    elif choice == '6':
        data[index] ['type_kuzov'] = input('vvedite new type_kuzova: ')
        flag = True
    elif choice == '7':
        data[index] ['probeg'] = input('vvedite new probeg: ')
        flag = True
    elif choice == '8':
        data[index] ['price'] = input('vvedite new price: ')

    else:
        print('invalid choice to update!!!')

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    if flag:
        return {'msg': 'updated', 'product':
        data[index]}
    else:
        return {'msg': 'not UPDATE!'}
def delete_product():
    data = get_data()
    id = int(input('vvedite id producta: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return {'msq': 'invalid id! product does not exist!'}
    index = data.index(product[0])
    deleted = data.pop(index)

    json.dump(data, open(FILE_PATH, 'w'))
    return{'msg': 'deleted!', 'product': deleted}
