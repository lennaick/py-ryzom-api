import unittest

if __name__ == '__main__':
    tests_lst = unittest.TestLoader().discover('tests', pattern='*_test.py')
    unittest.TextTestRunner().run(tests_lst)
