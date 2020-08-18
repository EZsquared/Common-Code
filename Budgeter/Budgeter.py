import pandas as pd
import re
from matplotlib import pyplot as plt

months = {"01": "January",
        "02":"February", 
        "03":"March",
        "04":"April",
        "05":"May", 
        "06":"June", 
        "07":"July", 
        "08":"August", 
        "09":"September", 
        "10":"October", 
        "11":"November", 
        "12":"December", }
dataSet = {'20':{}}

class Statementdb():
    def __init__(self, name, path =(r"C:\\Users\\Americ-da\\Documents\\Statements\\")):
        self.openFile(name)
        self.name = name
        self.fileName = ".".join([name, "csv"])
        self.state = pd.read_csv(path + self.fileName)
        self.transfers = self.state[self.state['Transaction Category'] == 'Transfer'].index
        self.state.drop(self.transfers, inplace = True)


        self.credits= self.state.loc[self.state['Transaction Type'] == 'Credit']
        self.debits= self.state.loc[self.state['Transaction Type'] == 'Debit']
        self.spent = (round(sum(self.debits['Amount']), 2))
        self.earned = (round(sum(self.credits['Amount']), 2))
        self.net = round((self.earned + self.spent), 2)
        self.addtoList(self.year, self.month, self.earned, self.spent, self.net)
    
    def addtoList(self, year, month, earned, spent, net):
        dataSet[year][month] = [earned, spent, net]

    def openFile(self, name):
        r = name.split("-")
        self.month = r[0]
        self.year = r[1]

def plotThis():
    x_axis = []
    y_axis_1 = []
    y_axis_2 = []
    y_axis_3 = []

    for i in sorted(dataSet):
        for values in sorted(dataSet[i]):
            x_axis.append(months[values])
            y_axis_1.append(dataSet[i][values][0])
            y_axis_2.append(dataSet[i][values][1])
            y_axis_3.append(dataSet[i][values][2])

    plt.style.use('seaborn')

    plt.bar(x_axis, y_axis_1, label = 'Earned')
    plt.bar(x_axis, y_axis_2, label = 'Spent')
    plt.plot(x_axis, y_axis_3, color ='#fc1303', label = 'Net')

    plt.ylabel('US$')
    plt.title('Net $ by Month')
    plt.legend()
    plt.grid(True)
    plt.show()

july20 = Statementdb('07-20')
june20 = Statementdb('06-20')
may20 = Statementdb('05-20')
april20 = Statementdb('04-20')
march0 = Statementdb('03-20')
february20 = Statementdb('02-20')
january20 = Statementdb('01-20')
plotThis()


