import shutil


def rollback(
        backup_file,
        target_file):

    shutil.copy(
        backup_file,
        target_file
    )

    return True