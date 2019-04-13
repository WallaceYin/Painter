from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class PaintBoard(QWidget):
    #PainterBoard widget
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__board = QPixmap(self.__size())
        self.__board.fill(Qt.white)
        
        self.__IsEmpty = True
        #self.EraserMode = False
        #self.RectangleMode = False
        self.Mode = 'draw'

        self.__lastPos = QPoint(0,0)
        self.__currentPos = QPoint(0,0)
        #self.__painter = QPainter()
        
        self.__thickness = 10
        self.__penColor = QColor("black")
        self.__colorList = QColor.colorNames()

        self.__rectangleLast = None
        self.__circleLast = None

    def __size(self):
        return QSize(800, 800)

    def clear(self):
        self.__board.fill(Qt.white)
        self.update()

    def restore(self, path):
        self.__board = QPixmap(path)
        self.update()

    def setPenColor(self, color="black"):
        self.__penColor = QColor(color)
        
    def setPenThickness(self, thickness=10):
        self.__thickness = thickness
    
    def setEraserMode(self):
        self.Mode = 'eraser'

    def setDrawingMode(self):
        self.Mode = 'draw'

    def setRectangleMode(self):
        self.Mode = 'rectangle'
        self.__rectangleLast = None

    def isEmpty(self):
        return self.__IsEmpty
    
    def getContentAsQImage(self):
        image = self.__board.toImage()
        return image

    def paintEvent(self, paintEvent):
        self.__painter = QPainter()
        self.__painter.begin(self)
        self.__painter.drawPixmap(0,0,self.__board)
        self.__painter.end()
        
    def drawRect(self, x1, y1, x2, y2):
        #pen = QPen(self.__penColor, self.__thickness, Qt.SolidLine)
        self.__painter.drawRect(x1, y1, x2, y2)

    def mousePressEvent(self, mouseEvent):
        if self.Mode == 'draw' or self.Mode == 'eraser':
            self.__currentPos =  mouseEvent.pos()
            self.__lastPos = self.__currentPos
        if self.Mode == 'rectangle':
            if self.__rectangleLast == None:
                self.__rectangleLast = mouseEvent.pos()
            self.__currentPos = mouseEvent.pos()
            self.__lastPos = self.__currentPos
        
    def mouseMoveEvent(self, mouseEvent):
        self.__currentPos =  mouseEvent.pos()

        if self.Mode == 'draw' or self.Mode == 'eraser':
            self.__painter.begin(self.__board)
            if self.Mode == 'draw':
                self.__painter.setPen(QPen(self.__penColor,self.__thickness))
            elif self.Mode == 'eraser':
                self.__painter.setPen(QPen(Qt.white,10))
            self.__painter.drawLine(self.__lastPos, self.__currentPos)
            self.__painter.end()
            self.__lastPos = self.__currentPos
            self.update()
        elif self.Mode == 'rectangle':
            self.__painter.begin(self.__board)
            self.__painter.setPen(QPen(self.__penColor, self.__thickness))
            self.__painter.end()
            self.__lastPos = self.__currentPos
            self.update()
        
    def mouseReleaseEvent(self, mouseEvent):
        self.__IsEmpty = False
        if self.Mode == 'rectangle':
            self.__painter.begin(self.__board)
            self.__painter.setPen(QPen(self.__penColor, self.__thickness))
            self.drawRect(self.__rectangleLast.x(), self.__rectangleLast.y(), self.__lastPos.x() - self.__rectangleLast.x(), self.__lastPos.y() - self.__rectangleLast.y())
            self.__painter.end()
            self.__lastPos = self.__currentPos
            self.update()
            self.__rectangleLast = None