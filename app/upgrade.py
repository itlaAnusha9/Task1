import json


def execute_upgrade(
        file_path,
        new_config):

    with open(
            file_path,
            "w") as f:

        json.dump(
            new_config,
            f,
            indent=4
        )

    return True