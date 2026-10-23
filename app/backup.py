import shutil
from datetime import datetime


def create_backup(config_file):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    backup_file = (
        f"backups/backup_{timestamp}.json"
    )

    shutil.copy(
        config_file,
        backup_file
    )

    return backup_file