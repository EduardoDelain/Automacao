from datetime import datetime
import os.path
from GerarLog import settings

class Log:
    """
    Classe de crição para o log da automação
    """
    def mensagem(self, Msg: str) -> None:
        """
        Função de captura o atributo mensagem e o insere no Log da aplicação
        :param Msg: "Linha de texto a ser passada para o Log da aplicação"
        :return: "Sem retorno"
        """
        if self.Enable:
            if str(Msg) == '\n':
                linha = str(Msg)
            else:
                linha = datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + ' - ' + str(Msg)
            print(linha)
            if self.LogFile:
                if not os.path.isdir(self.Path):
                    os.makedirs(self.Path)
                file = open(self.FileName, mode='a')
                file.write(linha + "\n")
                file.close()

    def __init__(self):
        self.Enable = True
        self.LogFile = True
        self.Path = None
        self.FileName = None

    def setEnabled(self, Enabled=True):
        self.Enable = Enabled

    def setLogToFile(self, LogToFile=False):
        self.LogFile = LogToFile

    def setPath(self, Path=None):
        self.Path = Path

    def setFileName(self, FileName=None):
        self.FileName = FileName

log = Log()
log.setEnabled(Enabled=settings.CONFIG['LOGENABLED'])
log.setLogToFile(LogToFile=settings.CONFIG['LOGTOFILE'])
log.setPath(Path=settings.CONFIG['LOGPATH'])
log.setFileName(FileName=settings.CONFIG['LOGFILENAME'])