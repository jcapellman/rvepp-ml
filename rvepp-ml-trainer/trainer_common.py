import json
import os


def load_from_file(file_name: str, object_class):
    if not file_name:
        raise ValueError("file_name parameter must be set")

    if not os.path.isfile(file_name):
        print('Config file not found (' + file_name + '), using defaults...')

        return object_class()

    with open(file_name) as json_file:
        try:
            data = json.load(json_file)

            return object_class(**data)
        except ValueError as ve:
            print("Config file could not be loaded (due to: " + str(ve) + "}) , using defaults...")

            return object_class()
