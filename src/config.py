import os

ROOT_DIR = os.path.abspath(os.path.curdir)

CONFIG = {
    'STATIC_FOLDER': os.path.join(ROOT_DIR, 'init/swagger.json'),
    'DB_DIALECT': f'{os.getenv("DB_DIALECT")}',
    'DB_URL': f'{os.getenv("DB_URL")}'
}
