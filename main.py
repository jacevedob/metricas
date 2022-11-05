from PyQt5 import QtWidgets
from Views.Inicio_Sesion import Ui_Login
import Models.declarative_base as db
from Models.Model import *

def run():
    pass


#LLAMADO A LA PRIMERA VENTANA QUE DEBERIA APARECER (LOGIN)
if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    run()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

