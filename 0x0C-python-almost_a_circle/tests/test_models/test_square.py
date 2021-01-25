#!/usr/bin/python3
"""Unittest for Rectangle"""
import sys
import io
import unittest
from models.base import Base
from models.square import Square


class TestingSquare(unittest.TestCase):
    """ Testing Square """
    def test_square_size(self):
        """Testing Square Size"""
        with self.assertRaises(TypeError):
            s1 = Square("hello")

        with self.assertRaises(TypeError):
            s2 = Square([9, 6])

        with self.assertRaises(TypeError):
            s3 = Square((7, 3))

        with self.assertRaises(TypeError):
            s4 = Square({'k': 8})

        with self.assertRaises(ValueError):
            s5 = Square(0)

        with self.assertRaises(ValueError):
            s6 = Square(-7)

        with self.assertRaises(TypeError):
            s7 = Square(4.5)

        with self.assertRaises(TypeError):
            s8 = Square(float('NaN'))

        with self.assertRaises(TypeError):
            s9 = Square(float('inf'))

        with self.assertRaises(TypeError):
            s10 = Square(True)

        with self.assertRaises(TypeError):
            s11 = Square(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            s12 = Square()

        with self.assertRaises(TypeError):
            s13 = Square(5j)

        with self.assertRaises(TypeError):
            s14 = Square(1e100)

    def test_square_x(self):
        """Testing Square X"""
        with self.assertRaises(TypeError):
            s1 = Square(2, "hello")

        with self.assertRaises(TypeError):
            s2 = Square(2, [9, 6])

        with self.assertRaises(TypeError):
            s3 = Square(4, (7, 3))

        with self.assertRaises(TypeError):
            s4 = Square(4, {'k': 8})

        with self.assertRaises(ValueError):
            s5 = Square(6, -7)

        with self.assertRaises(TypeError):
            s6 = Square(2, 4.5)

        with self.assertRaises(TypeError):
            s7 = Square(4, float('NaN'))

        with self.assertRaises(TypeError):
            s8 = Square(6, float('inf'))

        with self.assertRaises(TypeError):
            s9 = Square(4, True)

        with self.assertRaises(TypeError):
            s10 = Square(1, 2, 3, 4, 5, 6)

        s11 = Square(9, 0)
        self.assertEqual(s11.x, 0)

        with self.assertRaises(TypeError):
            s12 = Square(2, 5j)

        with self.assertRaises(TypeError):
            s13 = Square(2, 1e100)

    def test_square_y(self):
        """Testing Square Y"""
        with self.assertRaises(TypeError):
            s1 = Square(2, 3, "hello")

        with self.assertRaises(TypeError):
            s2 = Square(2, 3, [9, 6])

        with self.assertRaises(TypeError):
            s3 = Square(4, 3, (7, 3))

        with self.assertRaises(TypeError):
            s4 = Square(4, 3, {'k': 8})

        with self.assertRaises(ValueError):
            s5 = Square(6, 3, -7)

        with self.assertRaises(TypeError):
            s6 = Square(2, 3, 4.5)

        with self.assertRaises(TypeError):
            s7 = Square(4, 3, float('NaN'))

        with self.assertRaises(TypeError):
            s8 = Square(6, 3, float('inf'))

        with self.assertRaises(TypeError):
            s9 = Square(4, 3, True)

        with self.assertRaises(TypeError):
            s10 = Square(1, 2, 3, 4, 5, 6)

        s11 = Square(9, 3, 0)
        self.assertEqual(s11.y, 0)

        with self.assertRaises(TypeError):
            s12 = Square(2, 2, 5j)

        with self.assertRaises(TypeError):
            s13 = Square(2, 3, 1e100)

    def test_areaSquare(self):
        """Test area Square"""
        sq = Square(4, 4)
        self.assertEqual(sq.area(), 16)

    def test6_reassign(self):
        """ test reasign values"""
        rect = Square(1, 2, 3, 4)
        rect.x = 1
        self.assertEqual(rect.x, 1)

        rect1 = Square(1, 2, 3, 4)
        rect1.size = 5
        self.assertEqual(rect1.size, 5)

        with self.assertRaises(ValueError):
            rect2 = Square(1, 2, 3, 4)
            rect2.size = -1

        with self.assertRaises(TypeError):
            rect3 = Square(1, 2, 3, 4)
            rect3.size = "hello"

        with self.assertRaises(TypeError):
            rect4 = Square(1, 2, 3, 4)
            rect4.size = [9, 6]

        with self.assertRaises(TypeError):
            rect5 = Square(1, 2, 3, 4)
            rect5.y = (7, 3)

        with self.assertRaises(TypeError):
            rect6 = Square(1, 2, 3, 4)
            rect6.size = {'k': 8}

        with self.assertRaises(ValueError):
            rect7 = Square(1, 2, 3, 4)
            rect7.size = 0

        rect1 = Square(1, 2, 3, 4)
        rect1.x = 0
        self.assertEqual(rect1.x, 0)

        with self.assertRaises(TypeError):
            rect8 = Square(1, 2, 3, 4)
            rect8.size = 4.5

        with self.assertRaises(TypeError):
            rect8 = Square(1, 2, 3, 4)
            rect8.size = float('NaN')

        with self.assertRaises(TypeError):
            rect9 = Square(1, 2, 3, 4)
            rect9.size = float('inf')

        with self.assertRaises(TypeError):
            rect9 = Square(1, 2, 3, 4)
            rect9.x = True

        with self.assertRaises(TypeError):
            rect10 = Square(1, 2, 3, 4)
            rect10.x = 5j

        with self.assertRaises(TypeError):
            rect11 = Square(1, 2, 3, 4)
            rect11.y = 1e100

    def test_Square_update(self):
        """Square testing update function"""
        sq1 = Square(7, 7, 7, 7)
        self.assertEqual(str(sq1), "[Square] (7) 7/7 - 7")

        sq2 = Square(7, 7, 7, 7)
        sq2.update(1, 1)
        self.assertEqual(str(sq2), "[Square] (1) 7/7 - 1")

        sq3 = Square(7, 7, 7, 7)
        MyList = [1, 2, 3]
        sq3.update(*MyList)
        self.assertEqual(str(sq3), "[Square] (1) 3/7 - 2")

        sq4 = Square(7, 7, 7, 7)
        MyList = [1, 2, 3, 4]
        sq4.update(*MyList)
        self.assertEqual(str(sq4), "[Square] (1) 3/4 - 2")

        sq5 = Square(7, 7, 7, 7)
        MyList = []
        sq5.update(*MyList)
        self.assertEqual(str(sq5), "[Square] (7) 7/7 - 7")

        sq6 = Square(7, 7, 7, 7)
        MyDict = {'size': 1}
        sq6.update(**MyDict)
        self.assertEqual(str(sq6), "[Square] (7) 7/7 - 1")

        sq7 = Square(7, 7, 7, 7)
        MyDict = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        sq7.update(**MyDict)
        self.assertEqual(str(sq7), "[Square] (1) 1/1 - 1")

        sq7.update()
        self.assertEqual(str(sq7), "[Square] (1) 1/1 - 1")

        with self.assertRaises(ValueError):
            sq8 = Square(2)
            sq8.update(1, -2)

        with self.assertRaises(TypeError):
            sq9 = Square(2)
            sq9.update(1, 2.7)
        
        with self.assertRaises(TypeError):
            sq10 = Square(2)
            sq10.update(1, float('NaN'))

        with self.assertRaises(TypeError):
            sq11 = Square(2)
            sq11.update(1, float('inf'))

        with self.assertRaises(TypeError):
            sq12 = Square(2)
            sq12.update(1, 1e100)

        with self.assertRaises(TypeError):
            sq12 = Square(2)
            sq12.update(1, 5j)

        with self.assertRaises(TypeError):
            sq13 = Square(7, 7, 7, 7)
            sq13.update(1, True)

        with self.assertRaises(IndexError):
            sq14 = Square(7, 7, 7, 7)
            sq14.update(1, 2, 3, 4, 5)

    def test_str_Square(self):
        """Test str for Square"""
        with self.assertRaises(TypeError):
            sq1 = Square()
            sq1 = str(self)

        sq2 = Square(1)
        self.assertEqual(str(sq2), "[Square] (114) 0/0 - 1")

        sq3 = Square(1, 2)
        self.assertEqual(str(sq3), "[Square] (115) 2/0 - 1")
        
        sq4 = Square(1, 2 ,3)
        self.assertEqual(str(sq4), "[Square] (116) 2/3 - 1")
    
        sq5 = Square(1, 2, 3, 4)
        self.assertEqual(str(sq5), "[Square] (4) 2/3 - 1")

        with self.assertRaises(TypeError):
            sq6 = Square(1, 2, 3, 4, 5)
            sq6 = str(self)
        
        with self.assertRaises(TypeError):
            sq7 = Square(None)
            sq7 = str(self)

    def test1_Sq_todict(self):
        """Square test to_dictionary 1"""
        sq = Square(1, 2, 3, 4)
        sq1 = sq.to_dictionary()
        MyDict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        for i in MyDict:
            self.assertEqual(sq1[i], MyDict[i])
        
    def test2_Sq_todict(self):
        """Square test to_dictionary 2"""
        sq = Square(1)
        sq1 = sq.to_dictionary()
        MyDict = {'id': 69, 'size': 1, 'x': 0, 'y': 0}
        for i in MyDict:
            self.assertEqual(sq1[i], MyDict[i])

    def test3_Sq_todict(self):
        """Square test to_dictionary 3"""
        with self.assertRaises(TypeError):
            sq = Square()
            sq1 = sq.to_dictionary()

    def test4_Sq_todict(self):
        """Square test to_dictionary 4"""
        with self.assertRaises(TypeError):
            sq = Square(None)
            sq1 = sq.to_dictionary()

    def test11_update_kwargs(self):
        """ test updating kwargs square """
        r1 = Square(10, 10, 10, 10)
        r1.update(size=1)
        self.assertEqual(str(r1), "[Square] (10) 10/10 - 1")

        r2 = Square(10, 10, 10, 10)
        r2.update(size=3)
        self.assertEqual(str(r2), "[Square] (10) 10/10 - 3")

        with self.assertRaises(ValueError):
            r3 = Square(10, 10, 10, 10)
            r3.update(size=0)

        with self.assertRaises(ValueError):
            r4 = Square(10, 10, 10, 10)
            r4.update(x=-1)

        with self.assertRaises(TypeError):
            r5 = Square(10, 10, 10, 10)
            r5.update(size=4.2)

        with self.assertRaises(TypeError):
            r6 = Square(10, 10, 10, 10)
            r6.update(x=None)

        r2 = Square(10, 10, 10, 10)
        r2.update(x=1, sizet=4)
        self.assertEqual(str(r2), "[Square] (10) 1/10 - 10")

if __name__ == "__main__":
    unittest.main()
