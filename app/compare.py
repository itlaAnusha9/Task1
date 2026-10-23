def compare_configs(old_config, new_config):

    added = {}
    removed = {}
    modified = {}
    unchanged = {}

    for key in new_config:

        if key not in old_config:
            added[key] = new_config[key]

        elif old_config[key] != new_config[key]:
            modified[key] = {
                "old": old_config[key],
                "new": new_config[key]
            }

        else:
            unchanged[key] = new_config[key]

    for key in old_config:

        if key not in new_config:
            removed[key] = old_config[key]

    return {
        "added": added,
        "removed": removed,
        "modified": modified,
        "unchanged": unchanged
    }