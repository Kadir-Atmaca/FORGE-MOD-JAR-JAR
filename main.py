import os
if not os.path.exists("mods"):
    os.makedirs("mods")
import json
import zipfile
import shutil
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from main2 import Ui_MainWindow
import os
import webbrowser



class main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.tasarim = Ui_MainWindow()
        self.tasarim.setupUi(self)
        self.tasarim.pushButton_2_Githup.clicked.connect(self.web)
        self.tasarim.pushButton_baslat.clicked.connect(main.kont)
        self.tasarim.label.setText("Durum :")

    def kont():
     if os.path.exists("1.jar"):
        main.baslat()
     else:
        pencere.tasarim.label.setText("Durum : Hata lütfen içine eklenecek modu aynı programla aynı dizine atın ve ismini 1.jar yapın")
    def web(self):
        webbrowser.open('https://github.com/Kadir-Atmaca?tab=repositories')    
    
    def baslat():
     with zipfile.ZipFile("1.jar", 'r') as zip_ref:
      zip_ref.extractall("mod")
     n = 0;
     file_data = {"jars": []}
     for file_name in os.listdir("mods"):
        n = n+1
        file_info = {
            "identifier": {
                "group": "com."+file_name,
                "artifact": file_name.split('.')[0]
            },
            "version": {
                "range": "[1.0.0,)",
                "artifactVersion": "1.0.0"
            },
            "path": "META-INF/jarjar/"+file_name,
            "isObfuscated": False
        }
        file_data["jars"].append(file_info)
     json_data = json.dumps(file_data, indent=2)
     os.makedirs('mod/META-INF/jarjar')


     with open("mod/META-INF/jarjar/metadata.json", 'w') as file:
      file.write(json_data)
      files = os.listdir("mods/")
      for file in files:
       source_file = os.path.join("mods/", file)
       destination_file = os.path.join("mod/META-INF/jarjar/", file)
       shutil.copy(source_file, destination_file)

     with zipfile.ZipFile("mod.jar", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk("mod"):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "mod"))
     try:
        shutil.rmtree("mod")
     except OSError as e:
        print(f"Error: {e.strerror}")
     pencere.tasarim.label.setText("Durum : "+str(n)+" mod bulundu ve eklendi \nbaşarılı şekilde tamamlandı \n programın olduğu klasörde oluştu mod.jar")

        


app = QApplication([])
pencere = main()
pencere.show()
app.exec_()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 343)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_baslat = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_baslat.setFont(font)
        self.pushButton_baslat.setObjectName("pushButton_baslat")
        self.gridLayout.addWidget(self.pushButton_baslat, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pushButton_2_Githup = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2_Githup.setFont(font)
        self.pushButton_2_Githup.setObjectName("pushButton_2_Githup")
        self.gridLayout.addWidget(self.pushButton_2_Githup, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minecraft mod +mod "))
        self.pushButton_baslat.setText(_translate("MainWindow", "Başlat"))
        self.label_2.setText(_translate("MainWindow", "Lütfen Modlarınızı Mods Klasör Atın mods klasörü programla aynı dizinde bullunur"))
        self.pushButton_2_Githup.setText(_translate("MainWindow", "Githup"))
        self.label.setText(_translate("MainWindow", "Durum"))
        self.label_3.setText(_translate("MainWindow", "Lütfen hangi moda içine mod atacaksanız onu ismine 1.jar yapın ve programın \n"
"olduğu yere atın"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    








