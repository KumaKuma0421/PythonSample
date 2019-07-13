"""
標準ライブラリ logging
"logging"はログ出力するためのライブラリです。
ログはデフォルトではコンソールに表示されますが、ファイルに出力させることもできます。
"""

import logging

# ログの出力
logging.warning('これはログです。')

# 出力先をファイルに変更する。
logging.basicConfig(filename = 'hoge.log')
logging.error('これはログです。')

# 出力レベルの変更
logging.basicConfig(level = logging.DEBUG)
logging.debug('これは出力されます。')

"""
レベル
NOTSET(0)
DEBUG(10)
INFO(20)
WARNING(30)
ERROR(40)
CRITICAL(50)
"""

# ログの出力名を設定 (1)
logger = logging.getLogger('LoggingTest')

# ログレベルの設定 (2)
logger.setLevel(10)

# ログの出力先を設定 (3)
fh = logging.FileHandler('test.log')
logger.addHandler(fh)

# ログのコンソール出力の設定 (4)
sh = logging.StreamHandler()
logger.addHandler(sh)

# ログの出力形式の設定
formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.log(20, 'info')
logger.log(30, 'warning')
logger.log(100, 'test')

logger.info('info')
logger.warning('warning')