from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import sys

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        # Convert the string URL to a QUrl object
        self.browser.setUrl(QUrl("https://act.hoyolab.com/ys/app/interactive-map/index.html?lang=en-us#/map/2?shown_types=3,2,154&center=1115.79,-1251.00&zoom=-3.00"))
        self.setCentralWidget(self.browser)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)  # This keeps the window on top
        self.showMaximized()

app = QApplication(sys.argv)
window = Browser()
sys.exit(app.exec_())
