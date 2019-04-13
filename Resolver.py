from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CmdResolver(object):
    #Parse and resolve command lines

    def __init__(self):
        self.board = None
        
    def loadBoard(self,board):
        self.board = board

    def do(self, cmd):
        raise NotImplementedError