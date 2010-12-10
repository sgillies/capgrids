import unittest

from capgrids import box

class DataTestCase(unittest.TestCase):
    def test_csv(self):
        from capgrids import data
        self.failUnlessEqual(data['2'], [['2', 'Hibernia-Scandinavia', '5000', '-15.00', '30.00', '45.00', '65.00', 'a', 'I', '1', '4', '', '']])
        self.failUnlessEqual(data['87'], [['87', 'Cimmerius Bosphorus', '500', '35.00', '37.50', '44.50', '46.00', 'I', 'm', '1', '3', '', ''], ['87', 'Pontus-Phasis', '1000', '35.00', '43.00', '39.00', '44.00', 'a', 'h', '1', '5', '', '']])

class BoxTestCase(unittest.TestCase):
    def test_box_2(self):
        self.failUnlessEqual(box('2', 'G1'), (15.0, 60.0, 20.0, 65.0))
        self.assertRaises(IndexError, box, '2', 'G5')
    def test_box_87(self):
        self.failUnlessEqual(box('87', 'A1'), (35.0, 43.0, 36.0, 44.0))
        self.failUnlessEqual(box('87', 'I1'), (35.0, 45.5, 35.5, 46.0))
    def test_box_100(self):
        self.failUnlessEqual(box('100', 'Q4'), (40.0, 35.0, 45.0, 40.0))
    def test_box_102(self):
        self.failUnlessEqual(box('102', 'D4'), (20.0, 35.0, 25.0, 40.0))
    def test_box_inset(self):
        self.failUnlessEqual(box('82', 'inset'), (32.0, 16.0, 34.0, 17.0))

