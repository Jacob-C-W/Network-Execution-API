
def get_credentials(credential_profile: str):

    # proof of concept vault
    vault = {
        "salt": {
            "username": "admin",
            "password": "password"
        }
    }

    if credential_profile not in vault:
        raise Exception(
            f"Credential profile '{credential_profile}' not found"
        )

    return vault[credential_profile]
