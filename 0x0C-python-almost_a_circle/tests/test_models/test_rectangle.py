#!/usr/bin/python3
"""Unittest for Rectangle"""
import sys
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingRectangle(unittest.TestCase):
    """testing rectangle"""

    def test0_set_id(self):
        """id test rectangle"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(6, 5)
        r2 = Rectangle(14, 6, 3, 9, 5)
        r3 = Rectangle(1, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r3.id, 2)

    def test1_data_check_0(self):
        """data mal pasada WIDTH"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("hello", 2)

        with self.assertRaises(TypeError):
            r2 = Rectangle([9, 6], 2)

        with self.assertRaises(TypeError):
            r3 = Rectangle((7, 3), 4)

        with self.assertRaises(TypeError):
            r4 = Rectangle({'k': 8}, 5)

        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 6)

        with self.assertRaises(ValueError):
            r6 = Rectangle(-7, 8)

        with self.assertRaises(TypeError):
            r7 = Rectangle(4.5, 9)

        with self.assertRaises(TypeError):
            r8 = Rectangle(float('NaN'), 7)

        with self.assertRaises(TypeError):
            r9 = Rectangle(float('inf'), 7)

        with self.assertRaises(TypeError):
            r10 = Rectangle(True, 1)

        with self.assertRaises(TypeError):
            r11 = Rectangle(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(5j, 8)

        with self.assertRaises(TypeError):
            r14 = Rectangle(1e100, 7)

    def test2_data_check_0(self):
        """data mal pasada HEIGHT"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "hello")

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, [9, 6])

        with self.assertRaises(TypeError):
            r3 = Rectangle(4, (7, 3))

        with self.assertRaises(TypeError):
            r4 = Rectangle(5, {'k': 8})

        with self.assertRaises(ValueError):
            r5 = Rectangle(6, 0)

        with self.assertRaises(ValueError):
            r6 = Rectangle(8, -7)

        with self.assertRaises(TypeError):
            r7 = Rectangle(9, 4.5)

        with self.assertRaises(TypeError):
            r8 = Rectangle(7, float('NaN'))

        with self.assertRaises(TypeError):
            r9 = Rectangle(7, float('inf'))

        with self.assertRaises(TypeError):
            r10 = Rectangle(1, True)

        with self.assertRaises(TypeError):
            r11 = Rectangle(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(8, 5j)

        with self.assertRaises(TypeError):
            r14 = Rectangle(7, 1e100)

    def test3_data_check_0(self):
        """ mal data X """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "hello")

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, [9, 6])

        with self.assertRaises(TypeError):
            r3 = Rectangle(3, 4, (7, 3))

        with self.assertRaises(TypeError):
            r4 = Rectangle(4, 5, {'k': 8})

        with self.assertRaises(ValueError):
            r6 = Rectangle(6, 8, -7)

        with self.assertRaises(TypeError):
            r7 = Rectangle(7, 9, 4.5)

        with self.assertRaises(TypeError):
            r8 = Rectangle(8, 7, float('NaN'))

        with self.assertRaises(TypeError):
            r9 = Rectangle(9, 7, float('inf'))

        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 1, True)

        with self.assertRaises(TypeError):
            r11 = Rectangle(11, 1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(12, 8, 5j)

        with self.assertRaises(TypeError):
            r14 = Rectangle(13, 7, 1e100)

    def test3_data_check_1(self):
        """ data check """
        rect = Rectangle(9, 8, 0)
        self.assertEqual(rect.x, 0)

    def test4_data_check_0(self):
        """ mal data Y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 1, 2, "hello")

        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, [9, 6])

        with self.assertRaises(TypeError):
            r3 = Rectangle(4, 3, 4, (7, 3))

        with self.assertRaises(TypeError):
            r4 = Rectangle(5, 4, 5, {'k': 8})

        with self.assertRaises(ValueError):
            r6 = Rectangle(6, 6, 8, -7)

        with self.assertRaises(TypeError):
            r7 = Rectangle(7, 7, 9, 4.5)

        with self.assertRaises(TypeError):
            r8 = Rectangle(8, 8, 7, float('NaN'))

        with self.assertRaises(TypeError):
            r9 = Rectangle(9, 9, 7, float('inf'))

        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 10, 1, True)

        with self.assertRaises(TypeError):
            r11 = Rectangle(11, 1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            r12 = Rectangle()

        with self.assertRaises(TypeError):
            r13 = Rectangle(11, 12, 8, 5j)

        with self.assertRaises(TypeError):
            r14 = Rectangle(12, 13, 7, 1e100)

    def test4_data_check_0(self):
        """ data check """
        rect = Rectangle(9, 8, 6, 0)
        self.assertEqual(rect.y, 0)

    def test1_areaRect(self):
        """ test area"""
        rect = Rectangle(4, 4)
        self.assertEqual(rect.area(), 16)

    def test1_update(self):
        """ testing update """
        rect1 = Rectangle(7, 7, 7, 7, 7)
        self.assertEqual(str(rect1), "[Rectangle] (7) 7/7 - 7/7")

        rect2 = Rectangle(7, 7, 7, 7, 7)
        rect2.update(1, 1)
        self.assertEqual(str(rect2), "[Rectangle] (1) 7/7 - 1/7")

        rect3 = Rectangle(7, 7, 7, 7, 7)
        MyList = [1, 2, 3]
        rect3.update(*MyList)
        self.assertEqual(str(rect3), "[Rectangle] (1) 7/7 - 2/3")

        rect4 = Rectangle(7, 7, 7, 7, 7)
        MyList = [1, 2, 3, 4]
        rect4.update(*MyList)
        self.assertEqual(str(rect4), "[Rectangle] (1) 4/7 - 2/3")

        rect5 = Rectangle(7, 7, 7, 7, 7)
        MyList = []
        rect5.update(*MyList)
        self.assertEqual(str(rect5), "[Rectangle] (7) 7/7 - 7/7")

        rect6 = Rectangle(7, 7, 7, 7, 7)
        MyDict = {'width': 1, 'height': 1}
        rect6.update(**MyDict)
        self.assertEqual(str(rect6), "[Rectangle] (7) 7/7 - 1/1")

        rect7 = Rectangle(7, 7, 7, 7, 7)
        MyDict = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        rect7.update(**MyDict)
        self.assertEqual(str(rect7), "[Rectangle] (1) 1/1 - 1/1")

        rect7.update()
        self.assertEqual(str(rect7), "[Rectangle] (1) 1/1 - 1/1")

    def test2_update(self):
        """ test update """
        with self.assertRaises(TypeError):
            rect13 = Rectangle(7, 7, 7, 7, 7)
            rect13.update(1, True)

        with self.assertRaises(IndexError):
            rect14 = Rectangle(7, 7, 7, 7, 7)
            rect14.update(1, 2, 3, 4, 5, 6)

        with self.assertRaises(ValueError):
            rect8 = Rectangle(2, 2)
            rect8.update(1, -2)

        with self.assertRaises(TypeError):
            rect9 = Rectangle(2, 2)
            rect9.update(1, 2.7)

        with self.assertRaises(TypeError):
            rect10 = Rectangle(2, 2)
            rect10.update(1, float('NaN'))

        with self.assertRaises(TypeError):
            rect11 = Rectangle(2, 2)
            rect11.update(1, float('inf'))

        with self.assertRaises(TypeError):
            rect12 = Rectangle(2, 2)
            rect12.update(1, 1e100)

        with self.assertRaises(TypeError):
            rect12 = Rectangle(2, 2)
            rect12.update(1, 5j)

    def test_stRect(self):
        """ test str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle()
            rect1 = str(self)

        with self.assertRaises(TypeError):
            rect2 = Rectangle(1)
            rect2 = str(self)

    def test2_stRect(self):
        """ test str """
        rect3 = Rectangle(1, 2)
        self.assertEqual(str(rect3), "[Rectangle] (35) 0/0 - 1/2")

        rect4 = Rectangle(1, 2, 3)
        self.assertEqual(str(rect4), "[Rectangle] (36) 3/0 - 1/2")

        rect5 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect5), "[Rectangle] (5) 3/4 - 1/2")

    def test3_stRect(self):
        """ test str """
        with self.assertRaises(TypeError):
            rect6 = Rectangle(1, 2, 3, 4, 5, 6)
            rect6 = str(self)

        with self.assertRaises(TypeError):
            rect7 = Rectangle(None)
            rect7 = str(self)

    def test1_todictRect(self):
        """ test to_dictionary """
        rect = Rectangle(1, 2, 3, 4, 5)
        rect1 = rect.to_dictionary()
        MyDict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        for i in MyDict:
            self.assertEqual(rect1[i], MyDict[i])

    def test2_todictRect(self):
        """ test to_dictionary """
        rect = Rectangle(1, 2)
        rect1 = rect.to_dictionary()
        MyDict = {'id': 37, 'width': 1, 'height': 2, 'x': 0, 'y': 0}
        for i in MyDict:
            self.assertEqual(rect1[i], MyDict[i])

    def test3_todictRect(self):
        """ test to_dictionary """
        with self.assertRaises(TypeError):
            rect = Rectangle()
            rect1 = rect.to_dictionary()

    def test4_todictRect(self):
        """ test to_dictionary """
        with self.assertRaises(TypeError):
            rect = Rectangle(None)
            rect1 = rect.to_dictionary()

    def test5_reassign(self):
        """ test reasign values"""
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.x = 1
        self.assertEqual(rect.x, 1)

        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.width = 3
        self.assertEqual(rect1.width, 3)

        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.x = 0
        self.assertEqual(rect1.x, 0)

    def test6_reassign(self):
        """ test reasign values """
        with self.assertRaises(ValueError):
            rect2 = Rectangle(1, 2, 3, 4, 5)
            rect2.width = -1

        with self.assertRaises(TypeError):
            rect3 = Rectangle(1, 2, 3, 4, 5)
            rect3.width = "hello"

        with self.assertRaises(TypeError):
            rect4 = Rectangle(1, 2, 3, 4, 5)
            rect4.width = [9, 6]

        with self.assertRaises(TypeError):
            rect5 = Rectangle(1, 2, 3, 4, 5)
            rect5.y = (7, 3)

        with self.assertRaises(TypeError):
            rect6 = Rectangle(1, 2, 3, 4, 5)
            rect6.height = {'k': 8}

        with self.assertRaises(ValueError):
            rect7 = Rectangle(1, 2, 3, 4, 5)
            rect7.height = 0

        with self.assertRaises(TypeError):
            rect8 = Rectangle(1, 2, 3, 4, 5)
            rect8.height = 4.5

        with self.assertRaises(TypeError):
            rect8 = Rectangle(1, 2, 3, 4, 5)
            rect8.height = float('NaN')

        with self.assertRaises(TypeError):
            rect9 = Rectangle(1, 2, 3, 4, 5)
            rect9.height = float('inf')

        with self.assertRaises(TypeError):
            rect9 = Rectangle(1, 2, 3, 4, 5)
            rect9.x = True

        with self.assertRaises(TypeError):
            rect10 = Rectangle(1, 2, 3, 4, 5)
            rect10.x = 5j

        with self.assertRaises(TypeError):
            rect11 = Rectangle(1, 2, 3, 4, 5)
            rect11.y = 1e100

    def test11_update_kwargs(self):
        """ test updating kwargs rectangle """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (3) 10/10 - 10/1")

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(width=3)
        self.assertEqual(str(r2), "[Rectangle] (4) 10/10 - 3/10")

    def test12_update_kwargs(self):
        """ test updating kwargs """
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10, 10, 10)
            r3.update(width=0)

        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 10, 10, 10)
            r4.update(x=-1)

        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(width=4.2)

        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 10, 10, 10)
            r6.update(x=None)

        r2 = Rectangle(10, 10, 10, 10)
        r2.update(x=1, height=4, width=3)
        self.assertEqual(str(r2), "[Rectangle] (9) 1/10 - 3/4")

    def test_display_1(self):
        """test output 1"""
        r1 = Rectangle(2, 3)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        r1.display()
        self.assertEqual(captureOutput.getvalue(), ("##\n##\n##\n"))

    def test3_display_1(self):
        """ test output 3 """
        r9 = Rectangle(1, 1, 1, 1, 1)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        r9.display()
        self.assertEqual(captureOutput.getvalue(), ("\n #\n"))

    def test2_display_1(self):
        """ test output """
        with self.assertRaises(TypeError):
            """ test output 2 """
            r2 = Rectangle()
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r2.display()

        with self.assertRaises(TypeError):
            """ test output 3 """
            r3 = Rectangle(None)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r3.display()

        with self.assertRaises(TypeError):
            """ test output 4 """
            lista = []
            r4 = Rectangle(lista)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r4.display()

        with self.assertRaises(TypeError):
            """ test output 5 """
            r5 = Rectangle(1)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r5.display()

            r6 = Square(2, 2, 2)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r6.display()
            self.assertEqual(captureOutput.getvalue(), ("\n\n##\n##\n"))

            r7 = Rectangle(2, 3, 2)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r7.display()
            self.assertEqual(captureOutput.getvalue(), ("\n\n##\n##\n##\n"))

if __name__ == "__main__":
    unittest.main()
