import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from quamash import QEventLoop
from scanhost import manager
import asyncio


loop = QEventLoop(QApplication(sys.argv))
asyncio.set_event_loop(loop)
MainWindow = QMainWindow()
ui = mainwindow.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

QPushButton(ui.topFiller).setText("fre")

def on_reg(data):
    btn = QPushButton(ui.topFiller)
    btn.setText(data)
    btn.show()
    return 'hhahah'


def on_text(data):
    btn = QPushButton(ui.topFiller)
    btn.setText(data)
    btn.show()
    return f'一段文本{data}'


def listen():
    manager.reg_msg_handler('reg', on_reg)
    manager.reg_msg_handler('text', on_text)
    manager.listen()

listen()

# manager.heartbeat()
sys.exit(loop.run_forever())

