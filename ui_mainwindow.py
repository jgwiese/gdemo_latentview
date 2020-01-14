# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(692, 618)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.canvas = QLabel(self.centralWidget)
        self.canvas.setObjectName(u"canvas")
        self.canvas.setMinimumSize(QSize(512, 512))

        self.verticalLayout_2.addWidget(self.canvas)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalSlider_1 = QSlider(self.centralWidget)
        self.horizontalSlider_1.setObjectName(u"horizontalSlider_1")
        self.horizontalSlider_1.setMinimumSize(QSize(100, 0))
        self.horizontalSlider_1.setMinimum(-100)
        self.horizontalSlider_1.setMaximum(100)
        self.horizontalSlider_1.setTracking(False)
        self.horizontalSlider_1.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_1)

        self.horizontalSlider_2 = QSlider(self.centralWidget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(-100)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setTracking(False)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_2)

        self.horizontalSlider_3 = QSlider(self.centralWidget)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setMinimum(-100)
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setTracking(False)
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_3)

        self.horizontalSlider_4 = QSlider(self.centralWidget)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setMinimum(-100)
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setTracking(False)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_4)

        self.horizontalSlider_5 = QSlider(self.centralWidget)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setMinimum(-100)
        self.horizontalSlider_5.setMaximum(100)
        self.horizontalSlider_5.setTracking(False)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_5)

        self.horizontalSlider_6 = QSlider(self.centralWidget)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        self.horizontalSlider_6.setMinimum(-100)
        self.horizontalSlider_6.setMaximum(100)
        self.horizontalSlider_6.setTracking(False)
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_6)

        self.horizontalSlider_7 = QSlider(self.centralWidget)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        self.horizontalSlider_7.setMinimum(-100)
        self.horizontalSlider_7.setMaximum(100)
        self.horizontalSlider_7.setTracking(False)
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_7)

        self.horizontalSlider_8 = QSlider(self.centralWidget)
        self.horizontalSlider_8.setObjectName(u"horizontalSlider_8")
        self.horizontalSlider_8.setMinimum(-100)
        self.horizontalSlider_8.setMaximum(100)
        self.horizontalSlider_8.setTracking(False)
        self.horizontalSlider_8.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_8)

        self.horizontalSlider_9 = QSlider(self.centralWidget)
        self.horizontalSlider_9.setObjectName(u"horizontalSlider_9")
        self.horizontalSlider_9.setMinimumSize(QSize(0, 0))
        self.horizontalSlider_9.setMinimum(-100)
        self.horizontalSlider_9.setMaximum(100)
        self.horizontalSlider_9.setTracking(False)
        self.horizontalSlider_9.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_9)

        self.horizontalSlider_10 = QSlider(self.centralWidget)
        self.horizontalSlider_10.setObjectName(u"horizontalSlider_10")
        self.horizontalSlider_10.setMinimum(-100)
        self.horizontalSlider_10.setMaximum(100)
        self.horizontalSlider_10.setTracking(False)
        self.horizontalSlider_10.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_10)

        self.horizontalSlider_11 = QSlider(self.centralWidget)
        self.horizontalSlider_11.setObjectName(u"horizontalSlider_11")
        self.horizontalSlider_11.setMinimum(-100)
        self.horizontalSlider_11.setMaximum(100)
        self.horizontalSlider_11.setTracking(False)
        self.horizontalSlider_11.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_11)

        self.horizontalSlider_13 = QSlider(self.centralWidget)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setMinimum(-100)
        self.horizontalSlider_13.setMaximum(100)
        self.horizontalSlider_13.setTracking(False)
        self.horizontalSlider_13.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_13)

        self.horizontalSlider_14 = QSlider(self.centralWidget)
        self.horizontalSlider_14.setObjectName(u"horizontalSlider_14")
        self.horizontalSlider_14.setMinimum(-100)
        self.horizontalSlider_14.setMaximum(100)
        self.horizontalSlider_14.setTracking(False)
        self.horizontalSlider_14.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_14)

        self.horizontalSlider_12 = QSlider(self.centralWidget)
        self.horizontalSlider_12.setObjectName(u"horizontalSlider_12")
        self.horizontalSlider_12.setMinimum(-100)
        self.horizontalSlider_12.setMaximum(100)
        self.horizontalSlider_12.setTracking(False)
        self.horizontalSlider_12.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_12)

        self.horizontalSlider_16 = QSlider(self.centralWidget)
        self.horizontalSlider_16.setObjectName(u"horizontalSlider_16")
        self.horizontalSlider_16.setMinimum(-100)
        self.horizontalSlider_16.setMaximum(100)
        self.horizontalSlider_16.setTracking(False)
        self.horizontalSlider_16.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_16)

        self.horizontalSlider_15 = QSlider(self.centralWidget)
        self.horizontalSlider_15.setObjectName(u"horizontalSlider_15")
        self.horizontalSlider_15.setMinimum(-100)
        self.horizontalSlider_15.setMaximum(100)
        self.horizontalSlider_15.setTracking(False)
        self.horizontalSlider_15.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider_15)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 692, 20))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"reconstruction (grayscale) and segmentation (red)", None))
        self.canvas.setText(QCoreApplication.translate("MainWindow", u"canvas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"latent space components", None))
    # retranslateUi

