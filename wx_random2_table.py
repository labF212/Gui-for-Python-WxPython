import random
import time
import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(600, 400))
        
        self.temperatura = []
        self.humidade = []
        self.tabela_dados = []
        
        self.panel = wx.Panel(self)
        
        # Criando os elementos de interface gráfica
        self.label_temp = wx.StaticText(self.panel, label="Temperatura:")
        self.label_humid = wx.StaticText(self.panel, label="Humidade:")
        self.text_temp = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        self.text_humid = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        self.gauge_temp = wx.Gauge(self.panel, range=50, size=(300, 20), style=wx.GA_HORIZONTAL|wx.GA_SMOOTH)
        self.gauge_humid = wx.Gauge(self.panel, range=80, size=(300, 20), style=wx.GA_HORIZONTAL|wx.GA_SMOOTH)
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.gauge_temp.SetFont(font)
        self.gauge_humid.SetFont(font)
        self.list_ctrl = wx.ListCtrl(self.panel, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, "Data")
        self.list_ctrl.InsertColumn(1, "Hora")
        self.list_ctrl.InsertColumn(2, "Temperatura")
        self.list_ctrl.InsertColumn(3, "Humidade")
        
        # Posicionando os elementos na janela
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.label_temp, flag=wx.RIGHT, border=8)
        hbox1.Add(self.text_temp, proportion=1)
        hbox2.Add(self.gauge_temp, proportion=1, flag=wx.EXPAND)
        hbox3.Add(self.label_humid, flag=wx.RIGHT, border=8)
        hbox3.Add(self.text_humid, proportion=1)
        hbox4.Add(self.gauge_humid, proportion=1, flag=wx.EXPAND)
        hbox5.Add(self.list_ctrl, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox5, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        self.panel.SetSizer(vbox)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.atualizar_dados, self.timer)
        
        self.timer.Start(1000) # atualiza a cada 1 segundo
        
        self.Show()
    
    def atualizar_dados(self, event):
        # Gerando números aleatórios para temperatura e umidade
        nova_temp = round(random.uniform(0, 50), 2)
        nova_humid = round(random.uniform(20, 80), 2)
        
        # Atualizando as listas de temperatura e umidade
        self.temperatura.append(nova_temp)
        self.humidade.append(nova_humid)
        if len(self.temperatura) > 60:
            self.temperatura.pop(0)
        if len(self.humidade) > 60:
            self.humidade.pop(0)
        
        # Atualizando os valores de temperatura e umidade nos controles de texto
        self.text_temp.SetValue(str(nova_temp))
        self.text_humid.SetValue(str(nova_humid))
        
        # Atualizando as barras de progresso de temperatura e umidade
        self.gauge_temp.SetValue(int(nova_temp))
        self.gauge_humid.SetValue(int(nova_humid))

        # Atualizando a tabela com os últimos 10 números lidos
        self.tabela_dados.append((time.strftime("%d/%m/%Y"), time.strftime(" %H:%M:%S"), nova_temp, nova_humid))
        if len(self.tabela_dados) > 10:
            self.tabela_dados.pop(0)
        self.list_ctrl.DeleteAllItems()
        for i, (data, hora, temp, humid) in enumerate(self.tabela_dados):
            self.list_ctrl.InsertItem(i, data)
            self.list_ctrl.SetItem(i, 1, hora)
            self.list_ctrl.SetItem(i, 2, str(temp))
            self.list_ctrl.SetItem(i, 3, str(humid))


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, "Leitura de Dados")
    app.MainLoop()