ROLES = {

    "admin": [
        "compare",
        "validate",
        "backup",
        "upgrade",
        "rollback"
    ],

    "operator": [
        "compare",
        "validate"
    ],

    "viewer": [
        "view"
    ]
}


def authorize(
        role,
        action):

    return action in ROLES.get(
        role,
        []
    )