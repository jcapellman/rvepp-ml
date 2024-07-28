import unittest

from rvepp_ml_evaluator import evaluator_config


class TestsEvaluatorConfig(unittest.TestCase):
    def test_evaluator_config_null(self):
        with self.assertRaises(ValueError):
            evaluator_config.Config(False, '', '', '')

    if __name__ == '__main__':
        unittest.main()
