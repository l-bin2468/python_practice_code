# !/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def action(self, arg1, arg2):
        print(arg1, arg2)

    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.action(arg1, arg2)

        return func


def __generateTestCases():
    arglists = [('arg11', 'arg12'), ('arg21', 'arg22'), ('arg31', 'arg32')]
    for args in arglists:
        setattr(TestCases, 'test_func_%s_%s' % (args[0], args[1]),
                TestCases.getTestFunc(*args))


__generateTestCases()

if __name__ == '__main__':
    unittest.main()
