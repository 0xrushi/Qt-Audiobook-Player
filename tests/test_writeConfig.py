# run with python -m unittest tests/test_writeConfig.py
import unittest
from output import Ui_MainWindow
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os 
import ui_main
import sys
import hashlib
from time import sleep


class Test_writeConfig(unittest.TestCase):
    app = QApplication(sys.argv)
    def test_MainWindow_writeConfig(self):
        fileRenamed = False
        #   rename existing bookmarks file
        if os.path.exists("bookmarks.ini"):
            os.rename("bookmarks.ini","bookmarks.ini.tmp")
            fileRenamed = True
            sleep(1)

        classToTest = ui_main.MainWindow()
        #   setup things for the writeConfig function
        item0 = QListWidgetItem().setText("value0")
        item1 = QListWidgetItem().setText("value0")
        item2 = QListWidgetItem().setText("someMusic name and the timestamp 00:00:00")
        classToTest.listWidget_bookmark.addItem(item0)
        classToTest.listWidget_bookmark.addItem(item1)
        classToTest.listWidget_bookmark.addItem(item2)
        classToTest.full_file_path = "somefakePath/someSubdir/anothersubdir"
        classToTest.writeConfig()
        sleep(1)
        
        #   opening file hashing and checking equality
        file = open("bookmarks.ini",mode='r')
        fullText = file.read()
        file.close()
        hashObject = hashlib.md5(fullText.encode())
        bookmarksFileHash = hashObject.hexdigest()
        print(bookmarksFileHash)
        #   check hash of file against pregenerated file hash
        self.assertEqual(str(bookmarksFileHash),"45d54251222dabca81c6b69ae26eb1e0")
        os.remove("bookmarks.ini")

        if fileRenamed == True:
            print("worked")
            sleep(1)
            os.rename("bookmarks.ini.tmp","bookmarks.ini")
        