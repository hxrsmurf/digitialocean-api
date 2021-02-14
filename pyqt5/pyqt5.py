from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys
import gui
import requests
from datetime import datetime
import json

class PyQt5(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    #pyuic5 gui.ui -o gui.py
    def __init__(self, parent=None):
        super(PyQt5, self).__init__(parent)
        self.setupUi(self)
        
        self.iPAddressLineEdit.setText(self.myIP())        
        self.buttonLogin.clicked.connect(self.login)
        self.buttonLogout.clicked.connect(self.logout)
        
        self.domainInfo.itemPressed.connect(self.getRecords)      
        
        self.currentDate.setText(self.getDate())
        
        self.actionQuit.triggered.connect(self.quit)        
        self.buttonQuit.clicked.connect(self.quit)
        
    def login(self):
        self.setHeaders()
        self.aPIIDLineEdit.setEnabled(0)
        self.loginStatus.setText(self.account())
        self.getDropletInfo()
        self.listDomains()
        
    def setHeaders(self):
        api_url_base = 'https://api.digitalocean.com/v2/'
        headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.aPIIDLineEdit.text())}
        return (api_url_base, headers)
        
    def logout(self):
        self.aPIIDLineEdit.setEnabled(1)
        #self.accountInfo.setRowCount(0)
        #self.accountInfo.setColumnCount(0)
        self.clearInfo()
    
    def clearInfo(self):
        self.loginStatus.setText("Logged Out")
        #self.accountInfo.clear()
        #self.dropletInfo.clear()
        #self.domainInfo.clear()
        headers = None
    
    def quit(self):
        quit()
    
        
    def getRecords(self):
        getHeaders = self.setHeaders()   
        domain = self.domainInfo.currentItem().text()
        self.labeldomainRecordsInfo.setText(domain + " Records")
        
        api_url = getHeaders[0] + "domains/" + domain + "/records"
        
        response = requests.get(api_url, headers=getHeaders[1])
        domainsRecords = json.loads(response.content.decode('utf-8'))
        
        #self.tabledomainRecords.setRowCount(len(domainsRecords['domain_records']))
        self.tabledomainRecords.setRowCount(50)
        self.tabledomainRecords.setColumnCount(10)
        
        row = 0
        col = 0
        for key, domainInfo in enumerate(domainsRecords['domain_records']):
            #print('{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}:{8}:{9}'.format(v['id'],v['type'],v['name'],v['data'],v['priority'],v['port'],v['ttl'],v['weight'],v['flags'],v['tag']))
            
            for k,v in domainInfo.items():
                self.tabledomainRecords.setItem(row, col, QTableWidgetItem(str(v)))
                col += 1
            row += 1
            
    def account(self):
        getHeaders = self.setHeaders()
        api_url = '{0}account'.format(getHeaders[0])
        
        response = requests.get(api_url, headers=getHeaders[1])
        response = json.loads(response.content.decode('utf-8'))
        
        if (response['account']):
            #self.accountInfo.setRowCount(len(response['account']))
            self.accountInfo.setRowCount(7)
            self.accountInfo.setColumnCount(1)            
            self.accountInfo.setHorizontalHeaderLabels({"Value"})
            
            row = -1
            for key,value in (response['account']).items():        
                self.accountInfo.setItem(row,1, QTableWidgetItem(str(value)))
                self.accountInfo.setVerticalHeaderItem(row, QTableWidgetItem(key))
                row += 1
            return(response['account']['status'])
        else:
            return self.errorMessage()
    
    def listDomains(self):
        getHeaders = self.setHeaders()
        api_url = '{0}domains'.format(getHeaders[0])
        response = requests.get(api_url, headers=getHeaders[1])       
        
        domains = json.loads(response.content.decode('utf-8'))
        self.domainInfo.setRowCount(len(domains['domains']))
        self.domainInfo.setColumnCount(1)
        self.domainInfo.setHorizontalHeaderLabels({"Domain"})
        
        row = -1
        for k, v in enumerate(domains['domains']):
            self.domainInfo.setItem(row, 1, QTableWidgetItem(str(v['name'])))
            row += 1
            #print('{0}:{1}'.format(k, v['name']))
        
    def getDropletInfo (self):
        getHeaders = self.setHeaders()
        api_url = '{0}droplets'.format(getHeaders[0])
        
        response = requests.get(api_url, headers=getHeaders[1])
        droplets = json.loads(response.content.decode('utf-8'))
        
        self.dropletInfo.setRowCount(len(droplets['droplets']))
        self.dropletInfo.setColumnCount(3)
        
        row = 0
        col = 0
        for key, dropletInfo in enumerate(droplets['droplets']):
            for k, v in dropletInfo.items():                 
                if k == 'id' or k == 'networks' or k == 'name':                    
                    if k == 'networks':
                        v = v['v4'][0]['ip_address']
                    self.dropletInfo.setItem(row, col, QTableWidgetItem(str(v)))
                    self.dropletInfo.setHorizontalHeaderItem(col, QTableWidgetItem(str(k)))
                    col += 1
            row += 1
    
    def errorMessage(self):
        message = "Unable to authenticate you"
        self.loginStatus.setText(message)
        return (message)
        
    def myIP(self):
        response = requests.get("https://api.ipify.org").text
        return response
        
    def getDate(self):
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M")
        return dt_string

def main():
    app = QApplication(sys.argv)
    form = PyQt5()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()