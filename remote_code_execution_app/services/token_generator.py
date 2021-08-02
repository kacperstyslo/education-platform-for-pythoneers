import secrets


def generate_token() -> str:
    """
    Caller: remote_code_execution_app.views.CodeEditorView

    This method generates a unique token for the each user.
    """
    return secrets.token_hex(16)
