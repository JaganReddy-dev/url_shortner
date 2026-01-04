def find_user_uuid_by_url_id(url_store: dict, url_id):
    return next(
        (uuid for uuid, record in url_store.items() if record["unique_id"] == url_id),
        None,
    )


def find_user_uuid_by_api_key(user_store: dict, api_key):
    return next(
        (uuid for uuid, record in user_store.items() if record["api_key"] == api_key),
        None,
    )
