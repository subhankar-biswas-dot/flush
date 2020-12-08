# importing required libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys

#Creating MainWindow Class Which Inherits the Supper Class QMainWindow
class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        #creating the inheritance
        super(MainWindow,self).__init__(*args,**kwargs)
        #creating Tabs
        self.tabs=QTabWidget()
        #setting tabs at DocumentMode
        self.tabs.setDocumentMode(True)
        #when double clicked
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        #Tab is changed
        self.tabs.currentChanged.connect(self.tab_current_changed)
        #making current as closable
        self.tabs.setTabsClosable(True)
        #adding actionb when Tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        #Tabs As central Widgets
        self.setCentralWidget(self.tabs)
        #creating View
        #self.browser=QWebEngineView()
        #Initial Search Engine
        #self.browser.setUrl(QUrl("http://google.com"))
        #Adding New Url
        #self.browser.urlChanged.connect(self.update_urlbar)
        #When Loading gets over
        #self.browser.loadFinished.connect(self.update_title)
        #Setting as Central of Widgets
        #self.setCentralWidget(self.browser)
        #Creating a status bar
        self.status=QStatusBar()
        #Writting The Status
        self.setStatusBar(self.status)
        #Creating QToolBar for Navigation
        natv=QToolBar("Navigation")
        #adding Toolbar To main Window
        self.addToolBar(natv)
        #Adding Back Button and setting it
        back_btn=QAction("Back",self)
        #updating the the Status
        back_btn.setStatusTip("Moved Back")
        #back_btn.triggered.connect(self.browser.back)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        #Adding It in  the natv Bar
        natv.addAction(back_btn)
        #Next Button Configuratiuon
        Next_btn=QAction("Forward",self)
        Next_btn.triggered.connect(lambda:self.tabs.currentWidget().forward())
        #Update The Status
        Next_btn.setStatusTip("Went Forward")
        natv.addAction(Next_btn)
        #Adding The Reload Button
        reload_btn=QAction("Reload",self)
        reload_btn.triggered.connect(lambda: self.tabs.curentWidget().reload())
        #Update The Status
        reload_btn.setStatusTip("Site is Reloaded")
        natv.addAction(reload_btn)
        #Adding Home Button
        home_btn=QAction("Home",self)
        home_btn.triggered.connect(self.navigate_home)
        #Update The Status
        home_btn.setStatusTip("Going To Home")
        natv.addAction(home_btn)
        #Adding a separator
        natv.addSeparator()
        #Add Url
        self.urlbar=QLineEdit()
        #Adding Func When Button is Pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        natv.addWidget(self.urlbar)
        #Add Stop Button
        stop_btn=QAction("Stop",self)
        stop_btn.setStatusTip("Stop Loading")
        stop_btn.triggered.connect(lambda:self.tabs.currentWidget().stop())
        natv.addAction(stop_btn)
        #Adding First Tab
        self.add_new_tab(QUrl("http://google.com"),'HomePage')
        self.setWindowTitle("Subhankars Browser")
        #Add Tab Option
        self.show()
    def add_new_tab(self,qurl=None,lable="Blank"):
        if qurl is None:
            qurl=QUrl("http://google.com")
        browser=QWebEngineView()
        browser.setUrl(qurl)
        i=self.tabs.addTab(browser,lable)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser = browser: self.update_urlbar(qurl, browser))
        browser.loadFinished.connect(lambda _, i = i, browser = browser:self.tabs.setTabText(i, browser.page().title()))
    def tab_open_doubleclick(self,i):
        if i==-1:
            self.add_new_tab()
    def tab_current_changed(self,i):
        qurl=self.tabs.currentWidget().url()
        self.update_urlbar(self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())
    def close_current_tab(self, i):

        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return

        # else remove the tab
        self.tabs.removeTab(i)

    def update_title(self,browser):
        if browser!=self.tabs.currentWidget():
            return
        title=self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - Subhankars Browser"%title)
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
    def navigate_to_url(self):
        q=QUrl(self.urlbar.text())
        if q.scheme=="":
            q.setScheme("http")
        self.tabs.currentWidget().setUrl(q)
    def update_urlbar(self,q,browser=None):
        if browser!=self.tabs.currentWidget():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
#Creating QApplication
app=QApplication(sys.argv)
#Setting App Name
app.setApplicationName("Subhankars Browser")
#Creating The MainWindow Object
window=MainWindow()
#Creating Loop
app.exec_()
