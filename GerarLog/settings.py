from datetime import datetime

data = datetime.now()
path_log = 'Log/'
nome_log = path_log + data.strftime('%d-%m-%Y-%H-%M-%S') + '.txt'

CONFIG = {
    'LOGENABLED': True,
    'LOGTOFILE': True,
    'LOGPATH': path_log,
    'LOGFILENAME': nome_log
}