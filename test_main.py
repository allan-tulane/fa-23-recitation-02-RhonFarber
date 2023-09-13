from main import *


def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 40
  assert simple_work_calc(20, 3, 2) == 263.75
  assert simple_work_calc(30, 4, 2) == 930

  # 3 additional test cases
  assert simple_work_calc(2, 2, 2) == 4
  assert simple_work_calc(16, 2, 2) == 80
  assert simple_work_calc(8, 4, 2) == 120


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 31
  assert work_calc(20, 1, 2, lambda n: n * n) == 533.203125
  assert work_calc(30, 3, 2, lambda n: n) == 623.4375

  # 3 additional test cases
  assert work_calc(20, 3, 4, lambda n: 2) == 80
  assert work_calc(8, 2, 2, lambda n: 3 * n) == 96
  assert work_calc(12, 3, 3, lambda n: n - 2) == -32
