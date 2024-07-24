import unittest
import json

import trainer_dataset_config


class DataSetConfigTests(unittest.TestCase):
    def test_load_config_null_arg(self):
        with self.assertRaises(ValueError):
            trainer_dataset_config.load_config('')

    def test_load_config_invalid_path_arg(self):
        self.assertEqual(trainer_dataset_config.DataSetConfig(), trainer_dataset_config.load_config('/testo'))

    def test_load_config_bad_format_arg(self):
        with open ('testo', 'w') as file:
            file.write('test')

        self.assertEqual(trainer_dataset_config.DataSetConfig(), trainer_dataset_config.load_config('testo'))

    def test_load_config_valid_format_arg(self):
        with open ('testo', 'w') as file:
            file.write(json.dumps(trainer_dataset_config.DataSetConfig().__dict__))

        self.assertEqual(trainer_dataset_config.DataSetConfig(), trainer_dataset_config.load_config('testo'))


if __name__ == '__main__':
    unittest.main()
