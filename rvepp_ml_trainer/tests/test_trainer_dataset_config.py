import unittest
import json

from ..trainer_dataset_config import DataSetConfig


class DataSetConfigTests(unittest.TestCase):
    def test_load_config_null_arg(self):
        with self.assertRaises(ValueError):
            DataSetConfig.load_from_file('')

    def test_load_config_invalid_path_arg(self):
        self.assertEqual(DataSetConfig(), DataSetConfig.load_from_file('/testo'))

    def test_load_config_bad_format_arg(self):
        with open('testo', 'w') as file:
            file.write('test')

        self.assertEqual(DataSetConfig(), DataSetConfig.load_from_file('testo'))

    def test_load_config_valid_format_arg(self):
        with open('testo', 'w') as file:
            file.write(json.dumps(DataSetConfig().__dict__))

        self.assertEqual(DataSetConfig(), DataSetConfig.load_from_file('testo'))


if __name__ == '__main__':
    unittest.main()
