# coding=utf-8
import maya.cmds as mc
import maya.OpenMaya as om
import pymel.core as pm
from PySide2 import QtWidgets, QtCore, QtGui
class GEO_CHECK_UI(QtWidgets.QWidget):
    def __init__(self):
        super(GEO_CHECK_UI, self).__init__()
        self.setWindowTitle("CHECK WINDOW")
        self.buildUI()

    def buildUI(self):
        layout = QtWidgets.QGridLayout(self)
        self.item_1 = QtWidgets.QCheckBox("Check illegal face")
        self.item_1.toggled.connect(self.method_1)

        self.button_1 = QtWidgets.QPushButton('check')
        self.button_1.clicked.connect(self.check)

        self.button_2 = QtWidgets.QPushButton('select')
        self.button_2.clicked.connect(self.select)

        self.button_3 = QtWidgets.QPushButton('fix')
        self.button_3.clicked.connect(self.fix)

        layout.addWidget(self.item_1, 0, 0)
        layout.addWidget(self.button_1, 0, 2)
        layout.addWidget(self.button_2, 0, 3)
        layout.addWidget(self.button_3, 0, 4)

    def method_1(self):
        pass
    def check(self):
        '''
        非法面：多边面，零面，重合面，T型面
        使用API来获取面
        '''
        #多边面
        self.more_lst = []
        zero_lst = []
        num = 0
        iterator_1 = om.MItMeshPolygon(pm.PyNode(mc.ls(sl = True)[0]).__apiobject__())
        while not iterator_1.isDone():
            polygon = iterator_1.polygonVertexCount()
            item = iterator_1.currentItem()
            index = iterator_1.index()
            if polygon > 4:
                self.more_lst.append(mc.ls(sl = True)[0]+'.f[{0}]'.format(index))
                num = 1
            else:
                pass
            iterator_1.next()
        if num == 1:
            print("该模型有多边面！")
            print(self.more_lst)
        else:
            print('该模型没有多边面。')
        # FaceIntArray = om.MIntArray()
        # iterator_2 = om.MItMeshVertex(pm.PyNode(mc.ls(sl = True)[0]).__apiobject__())
        # while not iterator_2.isDone():
        #     FaceIndex = iterator_2.getConnectedFaces()
        #     point = iterator_2.position()
        #     print (point.x,point.y,point.z)
        #     zero_lst.append(point)
        #     num = num + 1
        #     iterator_2.next()
    def select(self):
        for item in self.more_lst:
            mc.select(item,add = True)
    def fix(self):
        pass
def showUI():
    ui = GEO_CHECK_UI()
    ui.show()
    return ui

ui = showUI()
