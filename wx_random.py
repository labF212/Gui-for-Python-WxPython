import random
import time
import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(400, 300))
        
        self.temperatura = []
        self.umidade = []
        
        self.panel = wx.Panel(self)
        
        # Criando os elementos de interface gráfica
        self.label_temp = wx.StaticText(self.panel, label="Temperatura:")
        self.label_umid = wx.StaticText(self.panel, label="Umidade:")
        self.text_temp = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        self.text_umid = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        
        # Posicionando os elementos na janela
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.label_temp, flag=wx.RIGHT, border=8)
        hbox1.Add(self.text_temp, proportion=1)
        hbox2.Add(self.label_umid, flag=wx.RIGHT, border=8)
        hbox2.Add(self.text_umid, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        self.panel.SetSizer(vbox)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.atualizar_dados, self.timer)
        self.timer.Start(1000) # atualiza a cada 1 segundo
        
        self.Show()
    
    def atualizar_dados(self, event):
        # Gerando números aleatórios para temperatura e umidade
        temp = random.randint(0, 50)
        hum = random.randint(20, 80)

        # Adicionando os dados às listas de temperatura e umidade
        self.temperatura.append(temp)
        self.umidade.append(hum)

        # Mantendo apenas os últimos 60 dados
        if len(self.temperatura) > 60:
            self.temperatura.pop(0)
            self.umidade.pop(0)

        # Atualizando os campos de temperatura e umidade na janela
        self.text_temp.SetValue(str(self.temperatura[-1]))
        self.text_umid.SetValue(str(self.umidade[-1]))

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, "Leitura de Dados")
    app.MainLoop()
