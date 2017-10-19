import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import addcontact_non_exec
class addcontact_class(addcontact_non_exec.Ui_Form, QtWidgets.QWidget):

    def __init__(self):
        super(addcontact_class, self).__init__()
        self.setupUi(self)


        regex_name = QtCore.QRegExp("[a-z-A-Z_]+")
        name_validator = QtGui.QRegExpValidator(regex_name)
        self.name_lineEdit.setValidator(name_validator)
        self.name_lineEdit = str(self.name_lineEdit.text())


        self.phone_lineEdit.setMaxLength(10)
        regex_phone = QtCore.QRegExp("[0-9_]+")
        phone_validator = QtGui.QRegExpValidator(regex_phone)
        self.phone_lineEdit.setValidator(phone_validator)


        regex_email = QtCore.QRegExp('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
        email_validator = QtGui.QRegExpValidator(regex_email)
        self.email_lineEdit.setValidator(email_validator)
        self.email_lineEdit = str(self.email_lineEdit)


        self.address_textEdit = str(self.address_textEdit)


        self.dob_dateEdit.setDisplayFormat('dd-MM-yyyy')
        self.dob_dateEdit.setCalendarPopup(True)
        self.dob_dateEdit.setDate(QtCore.QDate.currentDate())
        temp_dob = self.dob_dateEdit.date()
        DOB = temp_dob.toPyDate()
        print(DOB)














        self.btn_set_icon.clicked.connect(self.openFileNameDialog)
        self.btn_save.clicked.connect(self.save_action)




    def save_action(self):
        print("Save button clicked")
        addcontact_obj.hide()
        os._exit(0)
        #os.system('python phonebook_app.py')



    def openFileNameDialog(self):
        print("set icon clicked")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose Contact Icon", "", "Image Files (*.jpg *.png)", options=options)
        if fileName:
            print(fileName)
            pixmap = QtGui.QPixmap(fileName)
            self.contact_icon.setPixmap(pixmap)
            self.contact_icon.setScaledContents(True)





if __name__ == '__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    qapp.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    addcontact_obj = addcontact_class()
    addcontact_obj.show()
    qapp.exec_()