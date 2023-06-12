from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

app = QApplication([])
wind = QWidget()
wind.setWindowTitle('Memory Card')
wind.resize(1,1)
question = QLabel('')
answer = QPushButton('Ответить')
text_1 = QLabel('Ответ:')
text_2 = QLabel('Правильно! 1945Г')
correct = QLabel('Неправильно!')
box = QGroupBox('')
flag_1 = QRadioButton('')
flag_2 = QRadioButton('')
flag_3 = QRadioButton('')
flag_4 = QRadioButton('')
mistake = [flag_1,flag_2,flag_3,flag_4]
line_1 = QHBoxLayout()
line_2 = QVBoxLayout()
line_3 = QVBoxLayout()
line_3.addWidget(flag_1,alignment=Qt.AlignCenter)
line_3.addWidget(flag_3,alignment=Qt.AlignCenter)
line_2.addWidget(flag_2,alignment=Qt.AlignCenter)
line_2.addWidget(flag_4,alignment=Qt.AlignCenter)
line_1.addLayout(line_3)
line_1.addLayout(line_2)
box.setLayout(line_1)
box_answer = QGroupBox('')
box_1=QButtonGroup()
box_1.addButton(flag_1)
box_1.addButton(flag_2)
box_1.addButton(flag_3)
box_1.addButton(flag_4)
line_answer = QVBoxLayout()
line_answer.addWidget(text_1,alignment=Qt.AlignCenter)
line_answer.addWidget(text_2,alignment=Qt.AlignCenter)
box_answer.setLayout(line_answer)

line = QHBoxLayout()
line.addWidget(box)
line.addWidget(box_answer)
box_answer.hide()

line_4 = QVBoxLayout()
line_4.addWidget(question,alignment=Qt.AlignCenter)
line_4.addLayout(line)
line_4.addWidget(answer)

wind.setLayout(line_4)
def ans_answer():
    box.show()
    box_answer.hide()
    answer.setText('Ответить')
    box_1.setExclusive(False)
    flag_1.setChecked(False)
    flag_2.setChecked(False)
    flag_3.setChecked(False)
    flag_4.setChecked(False)
    box_1.setExclusive(True)
def next_question():
    box.hide()
    box_answer.show()
    answer.setText('Следующий вопрос')
class Vopros():
    def __init__(self,question1,right_answer,wrong1,wrong2,wrong3):
        self.question = question1
        self.save = right_answer
        self.fake_1 = wrong1
        self.fake_2 = wrong2
        self.fake_3 = wrong3

def ask(sefa):
    shuffle(mistake)
    mistake[0].setText(sefa.save)
    mistake[1].setText(sefa.fake_1)
    mistake[2].setText(sefa.fake_2)
    mistake[3].setText(sefa.fake_3)
    question.setText(sefa.question)
    text_2.setText(sefa.save)
    ans_answer()
many_objects =[]
sefa = Vopros('В каком году распался Советский союз?','1991Г','1945Г','2023Г','1999Г')
sefa_2 = Vopros('Какой танк принадлежит к Британии?','ФВ4005','т-100-лт','Маус','Шмаус')
sefa_3 = Vopros('Название шведского танка 10 уровня','Kranwagn','Progetto 65','Jacson','59-16')
sefa_4 = Vopros('Сколько стоит Dicker Max','2900','100','5','10000')
sefa_4 = Vopros('какого уровня Bofors Tornwagn?','8','4','10','6')
many_objects =[sefa,sefa_2,sefa_3,sefa_4]
def show_correct(res):
    text_1.setText(res)
    next_question()
def true_answer ():
    if mistake[0].isChecked():
        show_correct('Правильно!')
    else:
        if mistake[1].isChecked() or mistake[2].isChecked() or mistake[3].isChecked():
            show_correct('Неверно!')
timer = -1
def next_q():
    global timer,many_objects
    timer = timer+1
    if timer >= len(many_objects):
        timer = 0
    que = many_objects[timer]
    ask(que)
def click_tr():
    if answer.text() == 'Ответить':
        true_answer()
    else:
        next_q()

next_q()
answer.clicked.connect(click_tr)
wind.show()
app.exec_()
