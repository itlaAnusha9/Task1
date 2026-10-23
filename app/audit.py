from datetime import datetime


def log_action(
        user,
        action):

    timestamp = datetime.now()

    print(
        f"{timestamp} | "
        f"{user} | "
        f"{action}"
    )