"""Common checks that would go in every file."""

def check_common(check, maxx=100.0, miny=-20):
  """Common checks that would otherwise have to be repeated in every file."""
  check.dump_properties()
  check.assert_spinning()
  # Assumes a 7x10cm board with the origin at the upper-left
  check.assert_gt('min_x', check.min_x(), -2.0)
  check.assert_lt('max_x', check.max_x(), maxx)
  check.assert_gt('min_y', check.min_y(), miny)
  check.assert_lt('max_y', check.max_y(), 70.1)

  # maximum allowed z
  check.assert_lt('max_z', check.max_z(), 15.1)
