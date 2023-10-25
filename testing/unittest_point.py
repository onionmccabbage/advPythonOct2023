from using_unittest import Point

import unittest
# the name can be anything, but by convention...
class testPoint(unittest.TestCase):
    # we aim for each test to be independent
    def setUp(self):
        '''this will be run before each test'''
        super().setUp()
        self.point = Point(3, 5)
    def testMoveBy(self):
        '''test the moveBy method alters x and y correctly'''
        self.point.moveBy(5, 2)
        self.assertEqual(self.point.display, (8, 7))


if __name__ == '__main__':
    '''run our unit tests'''
    unittest.main()