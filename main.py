import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
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

def flush_user():
    [x.setParent(None) for x in ui.users.children()]
    i = 0
    for y, z in manager.get_hosts():
        label = QLabel(ui.users)
        label.setText(y[0])
        label.move(0, i * 10)
        i += 1
        label.show()

def get_text_from_editor():
    return ui.textEdit.toPlainText()

def get_button(data):
    btn = QPushButton(ui.history)
    btn.setText(data)
    btn.setMaximumWidth(300)
    btn.clicked.connect(lambda x: pyperclip.copy(data))
    return btn

def on_reg(data, proto):
    manager.reg(data['name'])
    flush_user()
    return 'success'

def on_text(data, proto):
    init_btn_history(data['msg'])

def init_btn_history(data):
    global label_height
    btn = get_button(data)
    btn.setText(data)
    btn.move(0, label_height)
    btn.show()
    label_height += btn.height()
    return f'success'


def listen():
    manager.reg_msg_handler('reg', on_reg)
    manager.reg_msg_handler('text', on_text)
    manager.listen()


def send_msg():
    data = get_text_from_editor()
    ui.textEdit.clear()
    init_btn_history(data)
    manager.send_msg(data)


ui.submit.clicked.connect(send_msg)
listen()
loop.create_task(manager.heartbeat(flush_user))
sys.exit(loop.run_forever())

