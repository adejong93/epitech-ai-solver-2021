# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/louisgrante/Code/epitech-ai-solver-2021/src/gui/template/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ai_solver(object):
    def setupUi(self, ai_solver):
        ai_solver.setObjectName("ai_solver")
        ai_solver.resize(637, 567)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ai_solver.setWindowIcon(icon)
        self.window = QtWidgets.QWidget(ai_solver)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.window.setFont(font)
        self.window.setObjectName("window")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.window)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setObjectName("main_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_layout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_layout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_layout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_layout.addItem(spacerItem3, 6, 2, 1, 1)
        self.goal_state_view = QtWidgets.QGridLayout(self.window)
        self.goal_state_view.setObjectName("goal_state_view")
        self.main_layout.addWidget(self.goal_state_view, 2, 2, 1, 1)
        self.current_state_view = QtWidgets.QGridLayout(self.window)
        self.current_state_view.setObjectName("current_state_view")
        self.main_layout.addWidget(self.current_state_view, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.main_layout.addItem(spacerItem4, 2, 0, 1, 1)
        self.goal_state_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.goal_state_label.setFont(font)
        self.goal_state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.goal_state_label.setObjectName("goal_state_label")
        self.main_layout.addWidget(self.goal_state_label, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_layout.addItem(spacerItem5, 3, 1, 1, 1)
        self.current_state_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.current_state_label.setFont(font)
        self.current_state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_state_label.setObjectName("current_state_label")
        self.main_layout.addWidget(self.current_state_label, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.main_layout.addItem(spacerItem6, 6, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.main_layout.addItem(spacerItem7, 2, 3, 1, 1)
        self.action_buttons = QtWidgets.QHBoxLayout()
        self.action_buttons.setObjectName("action_buttons")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.action_buttons.addItem(spacerItem8)
        self.next_state_button = QtWidgets.QToolButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_state_button.sizePolicy().hasHeightForWidth())
        self.next_state_button.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/louisgrante/Code/epitech-ai-solver-2021/src/gui/template/../../../../../Downloads/debug-step-over.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_state_button.setIcon(icon1)
        self.next_state_button.setObjectName("next_state_button")
        self.action_buttons.addWidget(self.next_state_button)
        self.pause_button = QtWidgets.QToolButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/louisgrante/Code/epitech-ai-solver-2021/src/gui/template/../../../../../Downloads/pause-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon2)
        self.pause_button.setIconSize(QtCore.QSize(14, 14))
        self.pause_button.setObjectName("pause_button")
        self.action_buttons.addWidget(self.pause_button)
        self.go_to_end_button = QtWidgets.QToolButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_to_end_button.sizePolicy().hasHeightForWidth())
        self.go_to_end_button.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/louisgrante/Code/epitech-ai-solver-2021/src/gui/template/../../../../../Downloads/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_to_end_button.setIcon(icon3)
        self.go_to_end_button.setIconSize(QtCore.QSize(14, 14))
        self.go_to_end_button.setObjectName("go_to_end_button")
        self.action_buttons.addWidget(self.go_to_end_button)
        self.reset_button = QtWidgets.QToolButton(self.window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/louisgrante/Code/epitech-ai-solver-2021/src/gui/template/../../../../../Downloads/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon4)
        self.reset_button.setIconSize(QtCore.QSize(14, 14))
        self.reset_button.setObjectName("reset_button")
        self.action_buttons.addWidget(self.reset_button)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.action_buttons.addItem(spacerItem9)
        self.main_layout.addLayout(self.action_buttons, 5, 1, 1, 1)
        self.metrics = QtWidgets.QFormLayout()
        self.metrics.setObjectName("metrics")
        self.nodes_nb_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nodes_nb_label.setFont(font)
        self.nodes_nb_label.setObjectName("nodes_nb_label")
        self.metrics.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nodes_nb_label)
        self.nodes_nb_value_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.nodes_nb_value_label.setFont(font)
        self.nodes_nb_value_label.setObjectName("nodes_nb_value_label")
        self.metrics.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nodes_nb_value_label)
        self.duration_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.duration_label.setFont(font)
        self.duration_label.setObjectName("duration_label")
        self.metrics.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.duration_label)
        self.duration_value_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.duration_value_label.setFont(font)
        self.duration_value_label.setObjectName("duration_value_label")
        self.metrics.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.duration_value_label)
        self.average_branching_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.average_branching_label.setFont(font)
        self.average_branching_label.setObjectName("average_branching_label")
        self.metrics.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.average_branching_label)
        self.average_branching_value_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.average_branching_value_label.setFont(font)
        self.average_branching_value_label.setObjectName("average_branching_value_label")
        self.metrics.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.average_branching_value_label)
        self.max_depth_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.max_depth_label.setFont(font)
        self.max_depth_label.setObjectName("max_depth_label")
        self.metrics.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.max_depth_label)
        self.max_depth_value_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.max_depth_value_label.setFont(font)
        self.max_depth_value_label.setObjectName("max_depth_value_label")
        self.metrics.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.max_depth_value_label)
        self.states_visited_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.states_visited_label.setFont(font)
        self.states_visited_label.setObjectName("states_visited_label")
        self.metrics.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.states_visited_label)
        self.states_visited_value_label = QtWidgets.QLabel(self.window)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setItalic(False)
        self.states_visited_value_label.setFont(font)
        self.states_visited_value_label.setObjectName("states_visited_value_label")
        self.metrics.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.states_visited_value_label)
        self.main_layout.addLayout(self.metrics, 5, 2, 1, 1)
        self.gridLayout_2.addLayout(self.main_layout, 0, 0, 1, 1)
        ai_solver.setCentralWidget(self.window)
        self.menubar = QtWidgets.QMenuBar(ai_solver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 24))
        self.menubar.setObjectName("menubar")
        self.submenu_solver = QtWidgets.QMenu(self.menubar)
        self.submenu_solver.setObjectName("submenu_solver")
        ai_solver.setMenuBar(self.menubar)
        self.submenu_solver_settings = QtWidgets.QAction(ai_solver)
        self.submenu_solver_settings.setObjectName("submenu_solver_settings")
        self.submenu_solver.addAction(self.submenu_solver_settings)
        self.menubar.addAction(self.submenu_solver.menuAction())

        self.retranslateUi(ai_solver)
        QtCore.QMetaObject.connectSlotsByName(ai_solver)

    def retranslateUi(self, ai_solver):
        _translate = QtCore.QCoreApplication.translate
        ai_solver.setWindowTitle(_translate("ai_solver", "AI Solver"))
        self.goal_state_label.setText(_translate("ai_solver", "Goal state"))
        self.current_state_label.setText(_translate("ai_solver", "Current state"))
        self.next_state_button.setText(_translate("ai_solver", "..."))
        self.pause_button.setText(_translate("ai_solver", "..."))
        self.go_to_end_button.setText(_translate("ai_solver", "..."))
        self.reset_button.setText(_translate("ai_solver", "..."))
        self.nodes_nb_label.setText(_translate("ai_solver", "Number of nodes"))
        self.nodes_nb_value_label.setText(_translate("ai_solver", "0"))
        self.duration_label.setText(_translate("ai_solver", "Duration"))
        self.duration_value_label.setText(_translate("ai_solver", "00:00:00"))
        self.average_branching_label.setText(_translate("ai_solver", "Average branching"))
        self.average_branching_value_label.setText(_translate("ai_solver", "0"))
        self.max_depth_label.setText(_translate("ai_solver", "Max depth"))
        self.max_depth_value_label.setText(_translate("ai_solver", "0"))
        self.states_visited_label.setText(_translate("ai_solver", "States visited"))
        self.states_visited_value_label.setText(_translate("ai_solver", "0"))
        self.submenu_solver.setTitle(_translate("ai_solver", "Solver"))
        self.submenu_solver_settings.setText(_translate("ai_solver", "Settings"))
import logo_rc
