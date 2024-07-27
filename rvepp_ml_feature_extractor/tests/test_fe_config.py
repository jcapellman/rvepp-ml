import unittest

from ..fe_config import Config


class ConfigTests(unittest.TestCase):
    def test_load_config_null_arg(self):
        with self.assertRaises(ValueError):
            Config(False, None, None, None)


if __name__ == '__main__':
    unittest.main()
