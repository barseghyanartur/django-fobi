__title__ = 'fobi.tests.test_dynamic_forms'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('FobiDataStructuresTest',)

import unittest

from copy import copy

from django.test import TestCase

from fobi.data_structures import SortableDict

from fobi.tests.base import print_info

class FobiDataStructuresTest(TestCase):
    """
    Tests of django-fobi ``data_structures`` module functionality.
    """
    def setUp(self):
        self.initial = SortableDict(
            [
                ('b', 1),
                ('a', 2),
                ('c', 3),
            ]
            )
        self.expected = SortableDict(
            [
                ('a', 2),
                ('b', 1),
                ('c', 3),
            ]
            )

    @print_info
    def test_01_sortable_dict_move_before_key(self):
        """
        Test the ``fobi.data_structures.SortableDict.move_before_key`` method.
        """
        flow = []

        flow.append(copy(self.initial))

        # Expected: a, b, c
        res = self.initial.move_before_key(source_key='a', target_key='b')
        self.assertTrue(res)

        flow.append(copy(self.initial))
        self.assertTrue(self.initial == self.expected)

        return flow

    @print_info
    def test_02_sortable_dict_move_after_key(self):
        """
        Test the ``fobi.data_structures.SortableDict.move_after_key`` method.
        """
        flow = []

        flow.append(copy(self.initial))

        res = self.initial.move_after_key(source_key='b', target_key='a') # Expected: a, b, c
        self.assertTrue(res)

        flow.append(copy(self.initial))
        self.assertTrue(self.initial == self.expected)

        return flow


if __name__ == '__main__':
    unittest.main()
