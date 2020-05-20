import unittest
from my_dict import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a = 1,b = 'test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
        d = Dict()
        d['hong'] = 1
        self.assertEqual(d.hong,1)
    def test_attr(self):
        d = Dict()
        d.fox = 'fox'
        self.assertEqual(d['fox'],'fox')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['none']
        with self.assertRaises(AttributeError):
            value = d.none


    