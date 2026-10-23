RULES = {

    "MaxUsers": {
        "min": 1,
        "max": 100000
    },

    "Timeout": {
        "min": 10,
        "max": 300
    }
}


def validate_config(config):

    errors = []

    for param, rule in RULES.items():

        if param in config:

            value = config[param]

            if value < rule["min"]:

                errors.append(
                    f"{param} below minimum limit"
                )

            if value > rule["max"]:

                errors.append(
                    f"{param} exceeds maximum limit"
                )

    return errors