from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from paintBoard import PaintBoard
from Resolver import CmdResolver

class Painter(QMainWindow):
# Main Painter window     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        #textEdit = QTextEdit()
        self.board = PaintBoard()
        self.setCentralWidget(self.board)
        # Actions

        self.cmdResolver = CmdResolver()
        self.cmdResolver.loadBoard(self.board)
        exitAction = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
 
        helpAction = QAction(QIcon('icons/help.png'), 'Help', self)
        helpAction.setShortcut('Ctrl+h')
        helpAction.setStatusTip('Help information')
        helpAction.triggered.connect(self.help)

        colorAction = QAction(QIcon('icons/color.png'), 'Color', self)
        colorAction.setStatusTip('Change the color')
        colorAction.triggered.connect(self.color)

        thicknessAction = QAction(QIcon(''), 'Thickness', self)
        thicknessAction.setStatusTip('Set the sickness of the line')
        thicknessAction.triggered.connect(self.thickness)

        penAction = QAction(QIcon('icons/pen.png'), 'Draw', self)
        penAction.setStatusTip('Click here to switch to drawing mode')
        penAction.triggered.connect(self.pen)

        paintAction = QAction(QIcon('icons/painter.png'), 'Paint', self)
        paintAction.setStatusTip('Click here to switch to painting mode')
        paintAction.triggered.connect(self.paint)

        circleAction = QAction(QIcon('icons/circle.png'), 'Circle', self)
        circleAction.setStatusTip('Click here to draw a circle')
        circleAction.triggered.connect(self.circle)

        polygonAction = QAction(QIcon('icons/polygon.png'), 'Polygon', self)
        polygonAction.setStatusTip('Polygon')
        polygonAction.triggered.connect(self.polygon)

        rectangleAction = QAction(QIcon('icons/rectangle.png'), 'Rectangle', self)
        rectangleAction.setStatusTip('Rectangle')
        rectangleAction.triggered.connect(self.rectangle)

        rubberAction = QAction(QIcon('icons/rubber.png'), 'Rubber', self)
        rubberAction.setStatusTip('Rubber')
        rubberAction.triggered.connect(self.rubber)

        clearAction = QAction(QIcon('icons/clear.png'), 'Clear', self)
        clearAction.setShortcut('Ctrl+l')
        clearAction.setStatusTip('Clear')
        clearAction.triggered.connect(self.board.clear)

        saveAction = QAction(QIcon('icons/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+s')
        saveAction.setStatusTip('Save')
        saveAction.triggered.connect(self.save)

        restoreAction = QAction(QIcon('icons/restore.png'), 'Restore', self)
        restoreAction.setShortcut('Ctrl+r')
        restoreAction.setStatusTip('Restore')
        restoreAction.triggered.connect(self.restore)

        cmdAction = QAction(QIcon('icons/cmd.png'), 'CommandLine', self)
        cmdAction.setShortcut('Ctrl+m')
        cmdAction.setStatusTip('Get command line from text box')
        cmdAction.triggered.connect(self.cmd)

        cmdFileAction = QAction(QIcon('icons/cmdfile.png'), 'CommandLineFile', self)
        cmdFileAction.setShortcut('Ctrl+n')
        cmdFileAction.setStatusTip('Get command line from file')
        cmdFileAction.triggered.connect(self.cmdFile)


        #Menu
        self.statusBar()
 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveAction)
        fileMenu.addAction(restoreAction)
        fileMenu.addAction(clearAction)
        fileMenu.addAction(exitAction)

        toolMenu = menubar.addMenu('&Tools')
        toolMenu.addAction(penAction)
        toolMenu.addAction(paintAction)
        toolMenu.addAction(rectangleAction)
        toolMenu.addAction(circleAction)
        toolMenu.addAction(polygonAction)
        toolMenu.addAction(rubberAction)

        cmdMenu = menubar.addMenu('&CommandLine')
        cmdMenu.addAction(cmdAction)
        cmdMenu.addAction(cmdFileAction)

        settingMenu = menubar.addMenu('&Settings')
        settingMenu.addAction(colorAction)
        settingMenu.addAction(thicknessAction)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(helpAction)

        #Tools
        toolbar = self.addToolBar('Draw')
        toolbar.addAction(penAction)
        toolbar.addAction(paintAction)
        toolbar.addAction(circleAction)
        toolbar.addAction(polygonAction)
        toolbar.addAction(rectangleAction)
        toolbar.addAction(rubberAction)
        toolbar.addAction(colorAction)
        toolbar = self.addToolBar('Save & Restore & clear')
        toolbar.addAction(clearAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(restoreAction)
        toolvar = self.addToolBar('Cmd')
        toolbar.addAction(cmdAction)
        toolvar.addAction(cmdFileAction)
        toolbar = self.addToolBar('Exit & Help')
        toolbar.addAction(helpAction)
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Main window')   
        self.show()

    def help(self):
        qtm = QMessageBox
        msg_box = qtm(qtm.Warning, u"Help", u"This is a GUI drawer program, you can freely draw whatever you want! For more usage, please check the README file",qtm.Yes| qtm.No)
        msg_box.exec_()
        if msg_box == qtm.Yes:
            self.label.setText("Question button/Ok")   
        elif msg_box == qtm.Cancel:   
            self.label.setText("Question button/Cancel")   
        else:   
            return

    def __size(self):
        return QSize(800, 800)

    def clear(self):
        self.__board.fill(Qt.white)
        self.update()

    def save(self):
        savePath = QFileDialog.getSaveFileName(self, 'Save Your Paint', 'untitle', '.bmp')
        if savePath[0] == "":
            return
        image = self.board.getContentAsQImage()
        image.save(savePath[0])

    def color(self, text):
        self.colorwidget = QWidget()
        self.colorwidget.setWindowTitle('Pen Color')
        self.colorwidget.resize(200,50)
        self.colorwidget.move(400, 400)
        combo = QComboBox(self.colorwidget)
        colors = ['red', 'green', 'yellow', 'blue', 'black']
        combo.addItems(colors)
        combo.activated[str].connect(self.board.setPenColor)
        combo.move(50, 10)
        self.colorwidget.show()

    def thickness(self):
        text, ok = QInputDialog.getText(self, 'Set thickness', 'Thickness:')
        if ok:
            self.board.setPenThickness(int(text))

    def restore(self):
        loadPath = QFileDialog.getOpenFileName(self, 'Load one paint', '.', 'All Files (*)')
        if loadPath[0] == '':
            return
        self.board.restore(loadPath[0])

    def pen(self):
        self.board.setDrawingMode()

    def paint(self):
        raise NotImplementedError

    def circle(self):
        raise NotImplementedError

    def polygon(self):
        raise NotImplementedError

    def rectangle(self):
        self.board.setRectangleMode()

    def rubber(self):
        self.board.setEraserMode()

    def cmd(self):
        text, ok = QInputDialog.getText(self, 'Command Line Box', 'Command')
        if ok:
            err = self.cmd.do(text)
            if (err == 1):
                self.qerror(text)
            

    def cmdFile(self):
        loadPath = QFileDialog.getOpenFileName(self, 'Load the command file', '.', 'All Files (*)')
        if loadPath[0] == '':
            return
        with open(loadPath[0], 'r') as f:
            for line in f:
                err = self.cmd.do(text)
                if (err == 1):
                    self.qerror(text)

    def qerror(self, msg):
        qtm = QMessageBox
        msg_box = qtm(qtm.Warning, u"Error", u"Error! The command <" + msg + "> cannot be resolved. Please Check your grammar and try again",qtm.Yes| qtm.No)
        msg_box.exec_()
        if msg_box == qtm.Yes:
            self.label.setText("Question button/Ok")   
        elif msg_box == qtm.Cancel:   
            self.label.setText("Question button/Cancel")   
        else:   
            return