
def null_validation(original_content, default_return):
    if original_content is None:
        return default_return
    else:
        return original_content