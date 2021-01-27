#!/usr/bin/python3
""" Unittest for base class """
import unittest
import sys
import io
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingBase(unittest.TestCase):
    """class for Test Base"""

    def testId(self):
        """test Id only"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(7)
        b4 = Base()
        b5 = Base(7)
        b6 = Base(-7)
        b7 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 7)
        self.assertEqual(b6.id, -7)
        self.assertEqual(b7.id, 4)

        self.assertEqual(str(type(Base)), "<class 'type'>")

        self.assertEqual(str(type(Rectangle)), "<class 'type'>")

        self.assertEqual(str(type(Square)), "<class 'type'>")

        r1 = Rectangle(2, 4)
        self.assertEqual(isinstance(r1, Rectangle), True)

        sq1 = Square(4)
        self.assertEqual(isinstance(sq1, Square), True)

        self.assertEqual(str(type(r1)), "<class 'models.rectangle.Rectangle'>")
        self.assertEqual(str(type(sq1)), "<class 'models.square.Square'>")
        self.assertEqual(issubclass(Square, Rectangle), True)
        self.assertEqual(issubclass(Square, Base), True)
        self.assertEqual(issubclass(Rectangle, Base), True)

        self.assertEqual(issubclass(Base, Rectangle), False)
        self.assertEqual(issubclass(Base, Square), False)

        r2 = Rectangle(4, 5)
        r3 = Rectangle(4, 5)
        self.assertEqual(r2 is r3, False)

        sq2 = Square(4)
        sq3 = Square(4)
        self.assertEqual(sq2 is sq3, False)

    def test1_to_json_string(self):
        """funct to pass to JSON string"""
        Base._Base__nb_objects = 0
        rect = Rectangle(5, 4, 3, 6)
        new_dict = rect.to_dictionary()
        jstrg = Base.to_json_string([new_dict])
        self.assertEqual(new_dict, {'y': 6, 'height': 4,
                                    'width': 5, 'x': 3, 'id': 1})
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(sorted(jstrg),
                         sorted('[{"height": 4, "x": 3, "width": '
                                '5, "y": 6, "id": 1}]'))
        self.assertEqual(type(jstrg), str)

    def test2_to_json_string(self):
        """funct to pass to JSON string"""
        Base._Base__nb_objects = 0
        new_dict = None
        jstrg = Base.to_json_string([new_dict])
        self.assertEqual(jstrg, '[null]')

    def test3_to_json_string(self):
        """funct to pass to JSON string"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

        jstrg = Base.to_json_string([])
        self.assertEqual(jstrg, "[]")

        MyList = [1, 2, 3]
        jstrg = Base.to_json_string([MyList])
        self.assertEqual(jstrg, "[[1, 2, 3]]")

        with self.assertRaises(NameError):
            MyString = "Hello"
            jstrg = Base.to_json_string(MyString)
            self.assertEqual(jstrg, Hello)

        i = (1, "foo", "bar")
        jsdict = Base.to_json_string(i)
        self.assertEqual(jsdict, '[1, "foo", "bar"]')

        Rect2 = Rectangle(5, 4)
        new_dict2 = Rect2.to_dictionary()
        jstrg = Base.to_json_string([new_dict2])
        self.assertEqual(new_dict2, {'y': 0, 'height': 4,
                                     'width': 5, 'x': 0, 'id': 1})

        with self.assertRaises(TypeError):
            Rect3 = Rectangle(1)
            new_dict3 = Rect3.to_dictionary()
            jstrg2 = Base.to_json_string([new_dict3])
            Base.to_json_string(jstrg2)

    def test1_jsonstr_to_dic(self):
        """ test json to dict """
        list_input1 = [
            {'id': 97, 'width': 5, 'height': 4},
            {'id': 79, 'width': 4, 'height': 5}
        ]
        json_list_input1 = Rectangle.to_json_string(list_input1)
        list_output1 = Rectangle.from_json_string(json_list_input1)
        self.assertEqual(list_output1, [{'height': 4, 'width': 5,
                                        'id': 97}, {'height': 5, 'width': 4,
                                                    'id': 79}])

        json_list_input2 = "[]"
        list_output2 = Rectangle.from_json_string(json_list_input2)
        self.assertEqual(list_output2, [])

        json_list_input3 = None
        list_output3 = Rectangle.from_json_string(json_list_input3)
        self.assertEqual(list_output3, [])

        with self.assertRaises(ValueError):
            json_list_input4 = "Hello Python"
            list_output4 = Rectangle.from_json_string(json_list_input4)
            self.assertEqual(list_output4, "")

        list_input5 = [
            {'id': 97, 'width': 5}
        ]
        json_list_input5 = Rectangle.to_json_string(list_input5)
        list_output5 = Rectangle.from_json_string(json_list_input5)
        self.assertEqual(list_output5, [{'id': 97, 'width': 5}])

    def test3_json_to_file1(self):
        """ test json string into file"""
        r1 = Rectangle(2, 4)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        lista = [{"id": 1, "width": 2, "y": 0, "x": 0, "height": 4},
                 {"id": 2, "width": 2, "y": 0, "x": 0, "height": 4}]
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test4_json_to_file2(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r1])
        lista = [{"id": 1, "x": 0, "width": 2, "y": 0, "height": 4}]
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test5_json_to_file3(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        s1 = Square(4, 5)
        s2 = Square(6, 7)
        s3 = Square(8, 9)
        Square.save_to_file([s1, s2, s3])
        lista = [{"x": 5, "size": 4, "id": 1, "y": 0},
                 {"x": 7, "size": 6, "id": 2, "y": 0},
                 {"x": 9, "size": 8, "id": 3, "y": 0}]
        with open("Square.json", "r") as file:
            file1 = file.read()
            list_output = Square.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test6_json_to_file4(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        Square.save_to_file([])
        lista = []
        with open("Square.json", "r") as file:
            file1 = file.read()
            list_output = Square.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test7_json_to_file5(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            MyString = "string"
            Square.save_to_file(MyString)

    def test8_json_to_file6(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            MyNum = 13
            Square.save_to_file(MyNum)

    def test9_json_to_file7(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            MyList = ["hello", "my", "friend"]
            Square.save_to_file(MyList)

    def test10_json_to_file8(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            Square.save_to_file([None])

    def test11_json_to_file9(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test12_json_to_file10(self):
        """ test json string into file """
        Base._Base__nb_objects = 0
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as MyFile:
            self.assertEqual(MyFile.read(), "[]")

    def test2_json_to_file(self):
        """ load from file """
        Base._Base__nb_objects = 0
        MyList = []
        Square.save_to_file(MyList)
        with open("Rectangle.json") as MyFile:
            self.assertEqual(MyFile.read(), "[]")

    def test13_json_to_file(self):
        """ load from file """
        Base._Base__nb_objects = 0
        Square.save_to_file(None)
        with open("Rectangle.json") as MyFile:
            self.assertEqual(MyFile.read(), "[]")
    
    def test14_json_to_file(self):
        """ load from file """
        with self.assertRaises(AttributeError):
            Square.save_to_string()

    def test1_dict_to_inst(self):
        """ dict to instance """
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")

        with self.assertRaises(TypeError):
            r10 = Rectangle()
            r10_dictionary = r10.to_dictionary()
            r20 = Rectangle.create(**r10_dictionary)

        with self.assertRaises(TypeError):
            r3 = Rectangle(None)
            r3_dictionary = r3.to_dictionary()
            r4 = Rectangle.create(**r3_dictionary)

        with self.assertRaises(TypeError):
            lista = []
            r5 = Rectangle.create(lista)

        with self.assertRaises(TypeError):
            r5 = Rectangle.create(2)

    def test_load_from_file(self):
        """ load from file test """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual([i.__dict__ for i in list_rectangles_input],
                         [i.__dict__ for i in list_rectangles_output])

    def test2_load_from_file(self):
        """ load from file """
        Base._Base__nb_objects = 0
        MyList = []
        Square.save_to_file(MyList)
        list_square_out = Square.load_from_file()
        self.assertEqual([i.__dict__ for i in MyList], 
                         [i.__dict__ for i in list_square_out])

    def test3_load_from_file(self):
        """ laod from file """
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json") is True:
            Square.save_to_file([])
        new = Square.load_from_file()
        self.assertEqual(new, [])
    
    def test4_load_from_file(self):
        """ load from file """
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json") is True:
            os.remove("Square.json")
        new = Square.load_from_file()
        self.assertEqual(new, [])
            

    def test_create0(self):
        """ test create funct """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect1 = Rectangle(3)
            rect1_dictionary = rect1.to_dictionary()
            rect2 = Rectangle.create(**rect1_dictionary)
    
    def test_create1(self):
        """ test create funct """
        Base._Base__nb_objects = 0
        rect1 = Rectangle(3, 5)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual((rect1 == rect2), False)
        self.assertEqual((rect1 is rect2), False)

    def test_create2(self):
        """ test create funct """
        Base._Base__nb_objects = 0
        rect1 = Rectangle(3, 5, 6)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual((rect1 == rect2), False)
        self.assertEqual((rect1 is rect2), False)

    def test_create2(self):
        """ test create funct """
        Base._Base__nb_objects = 0
        rect1 = Rectangle(3, 5, 6, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual((rect1 == rect2), False)
        self.assertEqual((rect1 is rect2), False)

    def test19_create1(self):
        """ test create method """
        s1 = Square.create(**{ 'id': 89 })
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 3")

        s2 = Square.create(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s2.__str__(), "[Square] (89) 0/0 - 1")

        s3 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s3.__str__(), "[Square] (89) 2/0 - 1")

        s4 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s4.__str__(), "[Square] (89) 2/3 - 1")

    def test_load_fromJson(self):
        """ error save to file"""
        with self.assertRaises(TypeError):
            Square.from_json_string()

    def test_json_to_file10(self):
        """ test json string into filee"""
        Base._Base__nb_objects = 0
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        list_sq_input = [s1, s2]
        Square.save_to_file(list_sq_input)
        with open("Square.json", "r") as my_file:
            list_sq_output = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(list_sq_output), my_file.read())


if __name__ == "__main__":
    unittest.main()
