import os

CONFIG = {
    'DB_DIALECT': f'{os.getenv("DB_DIALECT")}',
    'DB_URL': f'{os.getenv("DB_URL")}'
}
