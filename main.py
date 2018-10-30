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

label_count = 0

def get_text_from_editor():
    return ui.textEdit.toPlainText()

def get_button(data):
    btn = QPushButton(ui.topFiller)
    btn.setText(data)
    btn.clicked.connect(lambda x: pyperclip.copy(data))
    return btn

def on_reg(data):
    return 'success'

def on_text(data):
    global label_count
    btn = get_button(data)
    btn.setText(data)
    btn.move(0, label_count * 40)
    btn.show()
    label_count += 1
    return f'success'


def listen():
    manager.reg_msg_handler('reg', on_reg)
    manager.reg_msg_handler('text', on_text)
    manager.listen()

def send_msg():
    data = get_text_from_editor()
    ui.textEdit.clear()
    global label_count
    btn = get_button(data)
    btn.move(384, label_count * 40)
    btn.show()
    label_count += 1

ui.submit.clicked.connect(send_msg)
listen()

# manager.heartbeat()
sys.exit(loop.run_forever())

