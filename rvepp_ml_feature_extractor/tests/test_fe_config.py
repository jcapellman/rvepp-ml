import unittest

from rvepp_ml_feature_extractor import fe_config

class ConfigTests(unittest.TestCase):
    def test_load_config_null_arg(self):
        with self.assertRaises(ValueError):
            fe_config.Config(False, None, None, None)


if __name__ == '__main__':
    unittest.main()
