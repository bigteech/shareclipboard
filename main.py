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

label_count = 0

def on_reg(data):
    return 'success'

def on_text(data):
    global label_count
    btn = QPushButton(ui.topFiller)
    btn.setText(data)
    btn.move(0, label_count * 40)
    btn.show()
    label_count += 1
    return f'一段文本{data}'


def listen():
    manager.reg_msg_handler('reg', on_reg)
    manager.reg_msg_handler('text', on_text)
    manager.listen()

listen()

# manager.heartbeat()
sys.exit(loop.run_forever())

