#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    s1 = Rectangle(4, 5)
    s2 = Rectangle(6, 7)
    s3 = Rectangle(8, 9)
    Rectangle.save_to_file([s1, s2, s3])
    with open("Rectangle.json", "r") as file:
        file1 = file.read()
        list_output = Rectangle.from_json_string(file1)
        lista = [{'x': 0, 'width': 4, 'id': 1, 'height': 5, 'y': 0},
                {'x': 0, 'width': 6, 'id': 2, 'height': 7, 'y': 0},
                {'x': 0, 'width': 8, 'id': 3, 'height': 9, 'y': 0}]
    print(list_output)
    print(lista)
    
    if list_output == lista:
        print('son iguales')
    else:
        print('no')