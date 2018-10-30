import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from quamash import QEventLoop
from scanhost import manager
import asyncio
import pyperclip


loop = QEventLoop(QApplication(sys.argv))
asyncio.set_event_loop(loop)
MainWindow = QMainWindow()
ui = mainwindow.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

label_height = 0

def get_text_from_editor():
    return ui.textEdit.toPlainText()

def get_button(data):
    btn = QPushButton(ui.topFiller)
    btn.setText(data)
    btn.clicked.connect(lambda x: pyperclip.copy(data))
    return btn

def on_reg(data):
    return 'success'

def init_btn_history(data):
    global label_height
    btn = get_button(data)
    btn.setText(data)
    btn.move(0, label_height)
    btn.show()
    label_height += btn.height()
    return f'success'

def on_text(data):
    init_btn_history(data)


def listen():
    manager.reg_msg_handler('reg', on_reg)
    manager.reg_msg_handler('text', on_text)
    manager.listen()

def send_msg():
    data = get_text_from_editor()
    ui.textEdit.clear()
    init_btn_history(data)

ui.submit.clicked.connect(send_msg)
listen()

# manager.heartbeat()
sys.exit(loop.run_forever())

