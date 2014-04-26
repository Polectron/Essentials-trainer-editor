# -*- coding: utf8 -*-
#!/usr/bin/python

import os, sys, time, shutil
from PyQt4 import QtGui, QtCore, QtWebKit

dirIni = ""

class CompleteDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(CompleteDialog, self).__init__(parent)
        self.setWindowTitle("Error")
        self.width = 200
        self.height = 90
        self.setGeometry(0,0, self.width,self.height)
        self.setWindowIcon(QtGui.QIcon(os.path.join("data","icon.png")))
        self.resize(self.width,self.height)
        self.setMinimumSize(self.width,self.height)
        self.center()

        self.lbl1 = QtGui.QLabel('Faltan campos por rellenar.')

        self.layout = QtGui.QGridLayout(self)
        self.layout.addWidget(self.lbl1,0,0)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setWindowTitle("Configuracion")
        self.width = 400
        self.height = 150
        self.setGeometry(0,0, self.width,self.height)
        self.setWindowIcon(QtGui.QIcon(os.path.join("data","icon.png")))
        self.resize(self.width,self.height)
        self.setMinimumSize(self.width,self.height)
        self.center()

        self.lbl1 = QtGui.QLabel('Carpeta PBS:')
        self.lbl2 = QtGui.QLabel('El programa se cerrara para aplicar \nlos cambios.')
        self.lineed1 = QtGui.QLineEdit()
        self.lineed1.setReadOnly(True)
        self.btn1 = QtGui.QPushButton('Explorar...')
        self.btn1.clicked.connect(self.getPBS)
        self.btn2 = QtGui.QPushButton('Guardar')
        self.btn2.clicked.connect(self.savedata)

        self.layout = QtGui.QGridLayout(self)
        self.layout.addWidget(self.lbl1,0,0)
        self.layout.addWidget(self.lineed1,0,1)
        self.layout.addWidget(self.btn1,0,2)
        self.layout.addWidget(self.btn2,1,0)
        self.layout.addWidget(self.lbl2,1,1)


    def getPBS(self):
        self.dir = QtGui.QFileDialog.getExistingDirectory(self,"Open Directory","PBS",QtGui.QFileDialog.ShowDirsOnly);
        self.lineed1.setText(self.dir)

    def savedata(self):
        f = open(os.path.join('data','data.ini'),'w')
        f.write(self.dir)
        f.close
        exit()
        self.close()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


class editPokesWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(editPokesWindow, self).__init__(parent)
        self.pokes = ""
        l=QtGui.QVBoxLayout(self)
        l.setContentsMargins(0,0,0,0)
        l.setSpacing(0)

        self.s=QtGui.QScrollArea()
        l.addWidget(self.s)

        self.w=QtGui.QWidget(self)
        self.vbox=QtGui.QVBoxLayout(self.w)

        self.setGeometry(300, 200, 300, 400)
        self.setWindowTitle("Editar pokemons")

    def load(self):
        #print self.pokes
        count = 0
        self.w=QtGui.QWidget(self)
        self.vbox =QtGui.QVBoxLayout(self.w)
        self.wlist = []
        for i in range(0,self.pokenum):
            g = []
            p = self.pokes[count].split(',')
            count += 1
            g.append(QtGui.QLabel("Pokemon {0}:".format(count)))

            _l=QtGui.QGridLayout()
            _l.addWidget(g[-1],0,0)
            _l.addWidget(QtGui.QLabel("Especie:", self),1,1)
            _l.addWidget(QtGui.QLineEdit(),1,2)
            _l.addWidget(QtGui.QLabel("Nivel:", self),2,1)
            _l.addWidget(QtGui.QComboBox(self),2,2)
            self.wlist.append(_l)
            self.vbox.addLayout(_l)
        self.s.setWidget(self.w)


    def getPBS(self):
        self.dir = QtGui.QFileDialog.getExistingDirectory(self,"Open Directory","PBS",QtGui.QFileDialog.ShowDirsOnly);
        self.lineed1.setText(self.dir)

    def savedata(self):
        f = open(os.path.join('data','data.ini'),'w')
        f.write(self.dir)
        f.close
        exit()
        self.close()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


class editItemsWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(editItemsWindow, self).__init__(parent)
        self.setWindowTitle("Editar items")
        self.width = 300
        self.height = 450
        self.setGeometry(0,0, self.width,self.height)
        self.setWindowIcon(QtGui.QIcon(os.path.join("data","icon.png")))
        self.resize(self.width,self.height)
        self.setMinimumSize(self.width,self.height)
        self.center()

        self.lbl1 = QtGui.QLabel('Carpeta PBS:')
        self.lbl2 = QtGui.QLabel('El programa se cerrara para aplicar \nlos cambios.')
        self.lineed1 = QtGui.QLineEdit()
        self.lineed1.setReadOnly(True)
        self.btn1 = QtGui.QPushButton('Explorar...')
        self.btn1.clicked.connect(self.getPBS)
        self.btn2 = QtGui.QPushButton('Guardar')
        self.btn2.clicked.connect(self.savedata)

        self.layout = QtGui.QGridLayout(self)
        self.layout.addWidget(self.lbl1,0,0)
        self.layout.addWidget(self.lineed1,0,1)
        self.layout.addWidget(self.btn1,0,2)
        self.layout.addWidget(self.btn2,1,0)
        self.layout.addWidget(self.lbl2,1,1)


    def getPBS(self):
        self.dir = QtGui.QFileDialog.getExistingDirectory(self,"Open Directory","PBS",QtGui.QFileDialog.ShowDirsOnly);
        self.lineed1.setText(self.dir)

    def savedata(self):
        f = open(os.path.join('data','data.ini'),'w')
        f.write(self.dir)
        f.close
        exit()
        self.close()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.dir = ""
        self.width = 650
        self.height = 400
        self.setGeometry(0,0, self.width,self.height)
        self.setWindowTitle("Trainer editor")
        self.setWindowIcon(QtGui.QIcon(os.path.join("data","icon.png")))
        self.resize(self.width,self.height)
        self.setMinimumSize(self.width,self.height)
        self.center()
        self.dialogBox = MyDialog(self)
        self.itemsWindow = editItemsWindow(self)
        self.pokesWindow = editPokesWindow(self)
        self.completedialogBox = CompleteDialog(self)
        self.file1_1 = ""
        self.file2_1 = ""
        self.file3_1 = ""
        self.file4_1 = ""
        self.pokes = 0
        self.it = 0
        self.checkIni()

        # --- Menu --- #
        setings = QtGui.QAction("Opciones", self)
        setings.triggered.connect(self.openDialog)
        menu_bar = QtGui.QMenuBar()
        mfile = menu_bar.addMenu("&Archivo")
        mfile.addAction(setings)

        tab_widget = QtGui.QTabWidget()
        tab1 = QtGui.QWidget()
        tab2 = QtGui.QWidget()
        tab3 = QtGui.QWidget()

        p1_vertical = QtGui.QGridLayout(tab1)
        p2_vertical = QtGui.QFormLayout(tab2)
        p3_vertical = QtGui.QGridLayout(tab3)

        tab_widget.addTab(tab1, "Crear nuevo tipo de entrenador")
        tab_widget.addTab(tab2, "Editar entrenadores")
        tab_widget.addTab(tab3, "Sobre este programa")


        ##TAB 1
        self.lbl1_1 = QtGui.QLabel('Nombre:')
        self.lbl2_1 = QtGui.QLabel('Sysname:')
        self.lbl3_1 = QtGui.QLabel('Dinero/nivel (opcional):')
        self.lbl4_1 = QtGui.QLabel('BGM batalla (opcional):')
        self.lbl5_1 = QtGui.QLabel('BGM victoria (opcional):')
        self.lbl6_1 = QtGui.QLabel('ME comienzo batalla (opcional):')
        self.lbl7_1 = QtGui.QLabel('Sprite (opscional):')
        self.lbl8_1 = QtGui.QLabel('Genero:')
        self.lbl9_1 = QtGui.QTextBrowser(self)
        self.lbl9_1.append('Editando en \n{0}'.format(self.dir))

        self.btn1_1 = QtGui.QPushButton('Explorar...', self)
        self.btn1_1.clicked.connect(self.getBgm)

        self.btn2_1 = QtGui.QPushButton('Explorar...', self)
        self.btn2_1.clicked.connect(self.getBgmV)

        self.btn3_1 = QtGui.QPushButton('Explorar...', self)
        self.btn3_1.clicked.connect(self.getMe)

        self.btn4_1 = QtGui.QPushButton('Explorar...', self)
        self.btn4_1.clicked.connect(self.getSprite)

        self.btn5_1 = QtGui.QPushButton("Guardar")
        self.btn5_1.clicked.connect(self.save)


        self.combo1_1 = QtGui.QComboBox()
        self.combo1_1.addItem("Hombre")
        self.combo1_1.addItem("Mujer")
        self.combo1_1.addItem("Pareja")

        self.lineed1_1 = QtGui.QLineEdit()
        self.lineed1_1.connect(self.lineed1_1, QtCore.SIGNAL("textEdited(QString)"), self.sysname)
        self.lineed2_1 = QtGui.QLineEdit()
        self.lineed2_1.setReadOnly(True)
        self.lineed3_1 = QtGui.QLineEdit()
        self.lineed3_1.setReadOnly(True)
        self.lineed4_1 = QtGui.QLineEdit()
        self.lineed4_1.setReadOnly(True)
        self.lineed5_1 = QtGui.QLineEdit()
        self.lineed5_1.setReadOnly(True)
        self.lineed6_1 = QtGui.QLineEdit()
        self.lineed6_1.setReadOnly(True)

        self.status = QtGui.QStatusBar()
        self.status.showMessage('Ready')



        self.spin1_1 = QtGui.QSpinBox()
        self.spin1_1.setValue(80)
        self.spin1_1.setMaximum(255)

        p1_vertical.addWidget(self.lbl1_1,0,0)
        p1_vertical.addWidget(self.lineed1_1,0,1)

        p1_vertical.addWidget(self.lbl2_1,1,0)
        p1_vertical.addWidget(self.lineed2_1,1,1)

        p1_vertical.addWidget(self.lbl3_1,2,0)
        p1_vertical.addWidget(self.spin1_1,2,1)

        p1_vertical.addWidget(self.lbl4_1,3,0)
        p1_vertical.addWidget(self.lineed3_1,3,1)
        p1_vertical.addWidget(self.btn1_1,3,2)

        p1_vertical.addWidget(self.lbl5_1,4,0)
        p1_vertical.addWidget(self.lineed4_1,4,1)
        p1_vertical.addWidget(self.btn2_1,4,2)

        p1_vertical.addWidget(self.lbl6_1,5,0)
        p1_vertical.addWidget(self.lineed5_1,5,1)
        p1_vertical.addWidget(self.btn3_1,5,2)

        p1_vertical.addWidget(self.lbl7_1,6,0)
        p1_vertical.addWidget(self.lineed6_1,6,1)
        p1_vertical.addWidget(self.btn4_1,6,2)

        p1_vertical.addWidget(self.lbl8_1,7,0)
        p1_vertical.addWidget(self.combo1_1,7,1)

        p1_vertical.addWidget(self.btn5_1,8,0)

        p1_vertical.addWidget(self.lbl9_1,9,0)

        ##TAB 2
        self.lWidget = QtGui.QWidget()
        self.vBox = QtGui.QVBoxLayout()
        self.lWidget.setLayout(self.vBox)

        self.pokeWidget = QtGui.QWidget()
        self.pokeGrid = QtGui.QGridLayout()
        self.pokeWidget.setLayout(self.pokeGrid)

        self.itemWidget = QtGui.QWidget()
        self.itemGrid = QtGui.QGridLayout()
        self.itemWidget.setLayout(self.itemGrid)

        self.rWidget = QtGui.QWidget()
        self.grid = QtGui.QGridLayout()
        self.rWidget.setLayout(self.grid)

        self.rWidget.setDisabled(True)

        self.list1_2 = QtGui.QListWidget()
        t_l = []
        for i in self.getTrainers():
            l = i.split('\n')
            l.pop(0)
            l.pop(-1)
            self.list1_2.addItem(l[0]+'-'+l[1])
        self.list1_2.setCurrentRow (0)

        self.lbl6_2 = QtGui.QLabel('Editando:')
        self.lbl7_2 = QtGui.QLabel('asdf')
        self.btn1_2 = QtGui.QPushButton('Editar seleccionado')
        self.btn1_2.clicked.connect(self.editSelec)
        self.btn2_2 = QtGui.QPushButton('Nuevo entrenador')
        self.btn2_2.clicked.connect(self.newTr)
        self.lbl1_2 = QtGui.QLabel('Tipo:')

        self.combo1_2 = QtGui.QComboBox()
        tr = self.getTrainerTypes()
        tr.pop(0)
        tr.pop(-1)
        for i in tr:
            t = i.split(',')
            self.combo1_2.addItem(t[1])

        self.lbl2_2 = QtGui.QLabel('Nombre:')
        self.lineed1_2 = QtGui.QLineEdit()
        self.lbl3_2 = QtGui.QLabel('Aparicion No.:')
        self.lbl3_2.setToolTip('Si un entrenador aparece varias veces este numero indica que aparicion es.')
        self.spin1_2 = QtGui.QSpinBox()
        self.spin1_2.setMaximum(255)
        self.lbl4_2 = QtGui.QLabel('No. de pokemons:')
        self.spin2_2 = QtGui.QSpinBox()
        self.spin2_2.setMinimum(1)
        self.spin2_2.setMaximum(6)
        self.lbl5_2 = QtGui.QLabel('No. de items (opcional):')
        self.spin3_2 = QtGui.QSpinBox()
        self.spin3_2.setMaximum(8)
        self.lbl8_2 = QtGui.QLabel('Pokemons:')

        self.btn3_2 = QtGui.QPushButton('Guardar')
        self.btn3_2.clicked.connect(self.saveTr)

        self.btn4_2 = QtGui.QPushButton('Editar pokemons')
        self.btn4_2.clicked.connect(self.editPk)

        self.btn5_2 = QtGui.QPushButton('Editar items')
        self.btn5_2.clicked.connect(self.editIt)

        p2_vertical.addRow(self.lWidget,self.rWidget)
        self.vBox.addWidget(self.list1_2)
        self.vBox.addWidget(self.btn1_2)
        self.vBox.addWidget(self.btn2_2)
        self.vBox.addWidget(self.btn3_2)

        #self.grid.addWidget(self.lbl6_2,0,0)
        #self.grid.addWidget(self.lbl7_2,0,1)

        self.grid.addWidget(self.lbl1_2,1,0)
        self.grid.addWidget(self.combo1_2,1,1)

        self.grid.addWidget(self.lbl2_2,2,0)
        self.grid.addWidget(self.lineed1_2,2,1)

        self.grid.addWidget(self.lbl3_2,3,0)
        self.grid.addWidget(self.spin1_2,3,1)

        self.grid.addWidget(self.lbl4_2,4,0)
        self.grid.addWidget(self.spin2_2,4,1)

        self.grid.addWidget(self.lbl5_2,5,0)
        self.grid.addWidget(self.spin3_2,5,1)

        self.grid.addWidget(self.btn4_2,6,0)

        self.grid.addWidget(self.btn5_2,7,0)


        ##TAB 3
        self.lbl1_3 = QtGui.QLabel('Trainer editor es un editor de trainers para pokemon essentials desarrollado por Polectron,\npara facilitar la creacion de trainers, ya que las herramientas incluidas en Essentials\nson poco practicas.\r\n\n@2014-Polectron\r\n\nContacto: polectron@gmail.com')

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.append('Trainer editor es un editor de trainers para pokemon essentials desarrollado por Polectron,\npara facilitar la creacion de trainers, ya que las herramientas incluidas en Essentials\nson poco practicas.\r\nUsese bajo su propia responsabilidad, haga siempre backups de sus archivos.\r\n\n@2014-Polectron\r\n\nContacto: polectron@gmail.com')
        p3_vertical.addWidget(self.textBrowser,0,0)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(menu_bar)
        vbox.addWidget(tab_widget)

        self.setLayout(vbox)

    def editPk(self):
        self.pokesWindow.pokes = self.pokes
        self.pokesWindow.pokenum = self.spin2_2.value()
        self.pokesWindow.load()
        self.pokesWindow.exec_()
    def editIt(self):
        print'Editar item'
        self.itemsWindow.it = self.it
        print self.it
        self.itemsWindow.exec_()
    def saveTr(self):
        print'Guardando entrenador'
    def getExtension(self,f):
        f = f.split('/')
        f = f[-1]
        f = f.split('.')
        f = f[-1]
        return f
    def editSelec(self):
        #print'Editar seleccionado'
        #print self.list1_2.currentItem().text()
        #print self.list1_2.currentRow()
        self.rWidget.setDisabled(False)
        lt = []
        for i in self.getTrainers():
            l = i.split('\n')
            l.pop(0)
            l.pop(-1)
            lt.append(l)

        sysnm=  lt[self.list1_2.currentRow()].pop(0)
        ctr =  lt[self.list1_2.currentRow()].pop(0).split(',')
        pk_it = lt[self.list1_2.currentRow()].pop(0)

        self.pokes = lt[self.list1_2.currentRow()]

        pk_it = pk_it.split(',')


        pk = pk_it.pop(0)

        self.it = pk_it
        l = []
        tr = self.getTrainerTypes()
        tr.pop(0)
        tr.pop(-1)

        for i in tr:
            r = i.split(',')
            l.append(r[1])

        self.combo1_2.setCurrentIndex(l.index(sysnm))
        self.lineed1_2.setText(ctr[0])

        try:
            a = ctr[1]
        except:
            a = 0

        self.spin1_2.setValue(int(a))
        self.spin2_2.setValue(int(pk))
        self.spin3_2.setValue(len(self.it))


    def newTr(self):
        self.rWidget.setDisabled(False)
        self.combo1_2.setCurrentIndex(0)
        self.lineed1_2.setText("")
        self.spin1_2.setValue(0)
        self.spin2_2.setValue(1)
        self.spin3_2.setValue(0)

    def getTrainerTypes(self):
        f = open(self.dir+'\\trainertypes.txt','r')
        d = f.read()
        f.close()
        d = d.split('\n')
        return d
    def getTrainers(self):
        f = open(self.dir+'\\trainers.txt','r')
        d = f.read()
        f.close()
        d = d.split('#-------------------')
        d.pop(0)
        return d
    def getActualId(self):
        tr = self.getTrainerTypes()
        tr.pop(-1)
        tr = tr[-1]
        tr = tr.split(',')
        return tr[0]
    def checkIni(self):
        try:
            f = open(os.path.join('data','data.ini'),'r')
            self.dir = f.readline()
            f.close()
            if self.dir == "":
                self.openDialog()
        except:
            self.openDialog()

    def getBgm(self):
        self.file1_1 = QtGui.QFileDialog.getOpenFileName(self,
     "Explorar", "", "Image Files (*.mp3 *.wav *.mid *.ogg *.midi)");
        self.lineed3_1.setText(self.file1_1)
    def getBgmV(self):
        self.file2_1 = QtGui.QFileDialog.getOpenFileName(self,
     "Explorar", "", "Image Files (*.mp3 *.wav *.mid *.ogg *.midi)");
        self.lineed4_1.setText(self.file2_1)
    def getMe(self):
        self.file3_1 = QtGui.QFileDialog.getOpenFileName(self,
     "Explorar", "", "Image Files (*.mp3 *.wav *.mid *.ogg *.midi)");
        self.lineed5_1.setText(self.file3_1)
    def getSprite(self):
        self.file4_1 = QtGui.QFileDialog.getOpenFileName(self,
     "Explorar", "", "Image Files (*.png *.jpg *.jpeg *.bmp)");
        self.lineed6_1.setText(self.file4_1)
    def getSingleName(self,name):
        file1 = name.split('/')
        file1 = file1[-1]
        file1 = file1.split('.')
        file1 = file1[0]
        return file1
    def getRoot(self, r):
        r = r.split('\\')
        r.pop(-1)
        r = '\\'.join(r)
        return r
    def save(self):
        slash = '\\'
        if self.lineed1_1.text() != "" and self.spin1_1.value() != "":
            root = self.getRoot(self.dir)

            if self.file1_1 != "":
                file1 = self.getSingleName(self.file1_1)
                shutil.copy (str(self.file1_1), root+'\\Audio\\BGM')
            else:
                file1 = ""

            if self.file2_1 != "":
                file2 = self.getSingleName(self.file2_1)
                shutil.copy (str(self.file2_1), root+'\\Audio\\BGM')
            else:
                file2 = ""

            if self.file3_1 != "":
                file3 = self.getSingleName(self.file3_1)
                shutil.copy (str(self.file3_1), root+'\\Audio\\ME')
            else:
                file3 = ""

            if self.file4_1 != "":
                n = int(self.getActualId())+1
                digits = 3
                ns = str(n).zfill(digits)
                f = self.getExtension(self.file4_1)
                shutil.copy (str(self.file4_1), root+'\\Graphics\\Characters\\trainer'+str(ns)+'.'+f)

            if self.combo1_1.currentText() == 'Hombre':
                gender = 'Male'
            elif self.combo1_1.currentText() == 'Mujer':
                gender = 'Female'
            else:
                gender = 'Mixed'

            f = open(self.dir+'\\trainertypes.txt','a',0)
            f.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(int(self.getActualId())+1,self.lineed2_1.text(),self.lineed1_1.text(),self.spin1_1.value(),file1,file2,file3,gender))
            f.flush()
            os.fsync(f.fileno())
        else:
            self.openCompleteDialog()


    def openDialog(self):
        self.dialogBox.exec_()

    def openCompleteDialog(self):
        self.completedialogBox.exec_()

    def sysname(self,s):
        s = str(s)
        s = s.upper()
        s = s.split(' ')
        s = ''.join(s)
        self.lineed2_1.setText(s)
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


app = QtGui.QApplication(sys.argv)
frame = MainWindow()
frame.show()
sys.exit(app.exec_())