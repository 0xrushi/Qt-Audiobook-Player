# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maineSZGiI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1003, 905)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)
        self.graphicsView.setMinimumSize(QSize(0, 1))
        self.graphicsView.setMaximumSize(QSize(16777215, 1))

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_booktitle = QLabel(self.centralwidget)
        self.label_booktitle.setObjectName(u"label_booktitle")

        self.horizontalLayout_4.addWidget(self.label_booktitle)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_bookmark = QPushButton(self.centralwidget)
        self.pushButton_bookmark.setObjectName(u"pushButton_bookmark")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_bookmark.sizePolicy().hasHeightForWidth())
        self.pushButton_bookmark.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"icons/bookmark-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_bookmark.setIcon(icon)
        self.pushButton_bookmark.setIconSize(QSize(48, 48))

        self.verticalLayout_3.addWidget(self.pushButton_bookmark)

        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        icon1 = QIcon()
        icon1.addFile(u"icons/delete-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete.setIcon(icon1)
        self.pushButton_delete.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.pushButton_delete)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4.setStretch(0, 9)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_currenttime = QLabel(self.centralwidget)
        self.label_currenttime.setObjectName(u"label_currenttime")

        self.horizontalLayout_5.addWidget(self.label_currenttime)

        self.label_timeleft = QLabel(self.centralwidget)
        self.label_timeleft.setObjectName(u"label_timeleft")

        self.horizontalLayout_5.addWidget(self.label_timeleft)

        self.label_totaltime = QLabel(self.centralwidget)
        self.label_totaltime.setObjectName(u"label_totaltime")

        self.horizontalLayout_5.addWidget(self.label_totaltime)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.positionSlider = QSlider(self.centralwidget)
        self.positionSlider.setObjectName(u"positionSlider")
        self.positionSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.positionSlider)

        self.listWidget_bookmark = QListWidget(self.centralwidget)
        self.listWidget_bookmark.setObjectName(u"listWidget_bookmark")

        self.verticalLayout.addWidget(self.listWidget_bookmark)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_play = QPushButton(self.centralwidget)
        self.pushButton_play.setObjectName(u"pushButton_play")
        sizePolicy.setHeightForWidth(self.pushButton_play.sizePolicy().hasHeightForWidth())
        self.pushButton_play.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"icons/play-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_play.setIcon(icon2)
        self.pushButton_play.setIconSize(QSize(96, 96))

        self.gridLayout.addWidget(self.pushButton_play, 2, 1, 1, 1)

        self.pushButton_rightarrow = QPushButton(self.centralwidget)
        self.pushButton_rightarrow.setObjectName(u"pushButton_rightarrow")
        sizePolicy.setHeightForWidth(self.pushButton_rightarrow.sizePolicy().hasHeightForWidth())
        self.pushButton_rightarrow.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icons/fast-forward-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_rightarrow.setIcon(icon3)
        self.pushButton_rightarrow.setIconSize(QSize(96, 96))

        self.gridLayout.addWidget(self.pushButton_rightarrow, 2, 2, 1, 1)

        self.pushButton_rightfwd = QPushButton(self.centralwidget)
        self.pushButton_rightfwd.setObjectName(u"pushButton_rightfwd")
        sizePolicy.setHeightForWidth(self.pushButton_rightfwd.sizePolicy().hasHeightForWidth())
        self.pushButton_rightfwd.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"icons/rotate-right-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_rightfwd.setIcon(icon4)
        self.pushButton_rightfwd.setIconSize(QSize(96, 96))

        self.gridLayout.addWidget(self.pushButton_rightfwd, 4, 2, 1, 1)

        self.pushButton_bookselector = QPushButton(self.centralwidget)
        self.pushButton_bookselector.setObjectName(u"pushButton_bookselector")
        sizePolicy.setHeightForWidth(self.pushButton_bookselector.sizePolicy().hasHeightForWidth())
        self.pushButton_bookselector.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u"icons/menu-squared-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_bookselector.setIcon(icon5)
        self.pushButton_bookselector.setIconSize(QSize(96, 96))

        self.gridLayout.addWidget(self.pushButton_bookselector, 4, 1, 1, 1)

        self.pushButton_leftarrow = QPushButton(self.centralwidget)
        self.pushButton_leftarrow.setObjectName(u"pushButton_leftarrow")
        sizePolicy.setHeightForWidth(self.pushButton_leftarrow.sizePolicy().hasHeightForWidth())
        self.pushButton_leftarrow.setSizePolicy(sizePolicy)
        icon6 = QIcon()
        icon6.addFile(u"icons/rewind-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_leftarrow.setIcon(icon6)
        self.pushButton_leftarrow.setIconSize(QSize(96, 96))

        self.gridLayout.addWidget(self.pushButton_leftarrow, 2, 0, 1, 1)

        self.pushButton_leftfwd = QPushButton(self.centralwidget)
        self.pushButton_leftfwd.setObjectName(u"pushButton_leftfwd")
        sizePolicy.setHeightForWidth(self.pushButton_leftfwd.sizePolicy().hasHeightForWidth())
        self.pushButton_leftfwd.setSizePolicy(sizePolicy)
        icon7 = QIcon()
        icon7.addFile(u"icons/rotate-left-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_leftfwd.setIcon(icon7)
        self.pushButton_leftfwd.setIconSize(QSize(96, 96))

        self.gridLayout.addWidget(self.pushButton_leftfwd, 4, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        # self.horizontalLayout = QHBoxLayout()
        # self.horizontalLayout.setObjectName(u"horizontalLayout")
        # self.horizontalSpacer = QSpacerItem(40, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # self.horizontalLayout.addItem(self.horizontalSpacer)

        # self.pushButton_settings = QPushButton(self.centralwidget)
        # self.pushButton_settings.setObjectName(u"pushButton_settings")
        # sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        # sizePolicy2.setHorizontalStretch(0)
        # sizePolicy2.setVerticalStretch(0)
        # sizePolicy2.setHeightForWidth(self.pushButton_settings.sizePolicy().hasHeightForWidth())
        # self.pushButton_settings.setSizePolicy(sizePolicy2)
        # self.pushButton_settings.setMinimumSize(QSize(0, 10))

        # self.horizontalLayout.addWidget(self.pushButton_settings)


        # self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 7)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(1, 100)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1003, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_booktitle.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_bookmark.setText("")
        self.pushButton_delete.setText("")
        self.label_currenttime.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_timeleft.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_totaltime.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_play.setText("")
        self.pushButton_rightarrow.setText("")
        self.pushButton_rightfwd.setText("")
        self.pushButton_bookselector.setText("")
        self.pushButton_leftarrow.setText("")
        self.pushButton_leftfwd.setText("")
        # self.pushButton_settings.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

