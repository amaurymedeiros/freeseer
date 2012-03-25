#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2011  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/Freeseer/freeseer/

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import logging

from freeseer import project_info
from freeseer.frontend.qtcommon.Resource import resource_rc
from freeseer.framework.core import FreeseerCore

__version__= project_info.VERSION


class ReportDialog(QtGui.QWidget):
    """
    Failure report Dialog for the Freeseer Project. 

    """
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/freeseer/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        self.mainWidget = QtGui.QWidget()
        self.mainLayout = QtGui.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.infoLayout = QtGui.QFormLayout()
        self.mainLayout.addLayout(self.infoLayout)
        self.reportLayout = QtGui.QHBoxLayout()
        self.mainLayout.addLayout(self.reportLayout)
        self.buttonLayout = QtGui.QHBoxLayout()
        self.mainLayout.addLayout(self.buttonLayout)
        
        # Talk infomation
        self.titleLabel = QtGui.QLabel("Title:")
        self.titleLabel2 = QtGui.QLabel()
        self.speakerLabel = QtGui.QLabel("Speaker:")
        self.speakerLabel2 = QtGui.QLabel()
        self.eventLabel = QtGui.QLabel("Event:")
        self.eventLabel2 = QtGui.QLabel()
        self.roomLabel = QtGui.QLabel("Room:")
        self.roomLabel2 = QtGui.QLabel()
        self.timeLabel = QtGui.QLabel("Time:")
        self.timeLabel2 = QtGui.QLabel()
        self.infoLayout.addRow(self.titleLabel, self.titleLabel2)
        self.infoLayout.addRow(self.speakerLabel, self.speakerLabel2)
        self.infoLayout.addRow(self.eventLabel, self.eventLabel2)
        self.infoLayout.addRow(self.roomLabel, self.roomLabel2)
        self.infoLayout.addRow(self.timeLabel, self.timeLabel2)
        
        #Report
        self.commentLabel = QtGui.QLabel("Comment")
        self.commentEdit = QtGui.QLineEdit()
        
        self.reportCombo = QtGui.QComboBox()
        self.options = ['No Audio', 'No Video', 'No Audio/Video']
        for i in self.options:
            self.reportCombo.addItem(i)
        
        self.reportLayout.addWidget(self.commentLabel)
        self.reportLayout.addWidget(self.commentEdit)
        self.reportLayout.addWidget(self.reportCombo)
        
        #Buttons
        self.reportButton = QtGui.QPushButton("Report")
        self.closeButton = QtGui.QPushButton("Close")
        
        self.buttonLayout.addWidget(self.closeButton)
        self.buttonLayout.addWidget(self.reportButton)
        self.connect(self.closeButton, QtCore.SIGNAL("clicked()"), self.close)
