from unittest import TestCase
from board import Board
import numpy as np

class TestBoard(TestCase):
    def test_init(self):
        board = Board(2,3,1)
        np.testing.assert_array_equal(board.abstractLayer,
                         np.array([[1,0,0,0,1],
                                   [1,0,0,0,1],
                                   [1,0,0,0,1],
                                   [1,1,1,1,1]]))
    def test_update(self):
        self.fail()

    def test_restore(self):
        self.fail()

    def test_draw(self):
        self.fail()

    def test_cancellingLine(self):
        self.fail()
