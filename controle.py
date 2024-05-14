from PyQt5 import  uic,QtWidgets
import mysql.connector
import pywhatkit 
import time 

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mecanica"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.textEdit.toPlainText()

    print("CPF:",linha1)
    print("NOME:",linha2)
    print("TELEFONE",linha3)
    print("ENDEREÇO",linha4)
    print("PLACA",linha5)
    print("OBS:",linha6)
    linha2 = linha2.upper()
    linha4 = linha4.upper()
    linha5 = linha5.upper()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO clientes (CPF,NOME,TELEFONE,ENDERECO,PLACA,OBS) VALUES (%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.textEdit.clear()

def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM clientes"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 

def open_zap():
    zap.show()

def send_msg():
    telefone = zap.lineEdit.text()
    telefone = '+55' + telefone

    pywhatkit.sendwhatmsg_instantly(telefone,'O serviço do seu carro está pronto, venha buscá-lo.')





app = QtWidgets.QApplication([])
formulario = uic.loadUi("telaprincipal.ui")
segunda_tela = uic.loadUi("tela_secundaria.ui")
zap = uic.loadUi("zap.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(open_zap)
zap.pushButton.clicked.connect(send_msg)
formulario.show()
app.exec()
