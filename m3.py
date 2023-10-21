from PyQt5.QtWidgets import QWidget, QLineEdit,\
    QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()

lb_quest = QLabel("Ведіть запитання:")
lb_right_ans = QLabel("Ведіть правельну відповідь")
lb_wrong_ans1 = QLabel("Ведіть першу хибну відповідь")
lb_wrong_ans2 = QLabel("Ведіть другу хибну відповідь")
lb_wrong_ans3 = QLabel("Ведіть третю хибну відповідь")

le_qwestion = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()
lb_header_stat = QLabel("Статистика")
lb_statistic = QLabel()

v1_labels = QVBoxLayout()
v1_labels.addWidget(lb_quest)
v1_labels.addWidget(lb_right_ans)
v1_labels.addWidget(lb_wrong_ans1)
v1_labels.addWidget(lb_wrong_ans2)
v1_labels.addWidget(lb_wrong_ans3)

v1_lineEdits = QVBoxLayout()
v1_lineEdits.addWidget(le_qwestion)
v1_lineEdits.addWidget(le_right_ans)
v1_lineEdits.addWidget(le_wrong_ans1)
v1_lineEdits.addWidget(le_wrong_ans2)
v1_lineEdits.addWidget(le_wrong_ans3)

h1_qwestion =QHBoxLayout()
h1_qwestion.addLayout(v1_labels)
h1_qwestion.addLayout(v1_lineEdits)

btn_back = QPushButton('назад')
btn_add_qwestion = QPushButton('додати запитання')
btn_clear = QPushButton('очистити')

h1_buttons = QHBoxLayout()
h1_buttons.addWidget(btn_add_qwestion)
h1_buttons.addWidget(btn_clear)

v1_res = QVBoxLayout()
v1_res.addLayout(h1_qwestion)
v1_res.addLayout(h1_buttons)
v1_res.addWidget(lb_header_stat)
v1_res.addWidget(lb_statistic)
v1_res.addWidget(btn_back)
menu_win.setLayout(v1_res)
menu_win.resize(400, 300)
