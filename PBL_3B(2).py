import os
os.environ ["KIVY_AUDIO"] ="sdl2"
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

class Principal(BoxLayout):
    minha_imagem= StringProperty('inicial.jpg')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size= (400,600)
        self.som_aeronave=SoundLoader.load('somAeronave.mp3')
        self.som_carroca=SoundLoader.load('somCarroca.mp3')
        self.som_submarino=SoundLoader.load('somSubmarino.mp3')
        self.som_trem=SoundLoader.load('somTrem.mp3')
        self.som_triciclo=SoundLoader.load('somTriciclo.mp3')
        self.som_tuctuc=SoundLoader.load('somTuctuc.mp3')
        self.som_sair=SoundLoader.load('SomSair.wav')

    def selecione(self,text):
        if text == 'Aeronave':
            self.ids.mensagem.text= '[i][color=#FF3333]Até 280 km/h[/color][/i]'
            self.minha_imagem= 'aeronave.jpg'
            self.som_aeronave.play()
        elif text == 'Carroca':
            self.ids.mensagem.text= '[i][color=#FF3333]Até 28 km/h (2 cavalos)[/color][/i]'
            self.minha_imagem= 'carroca.jpg'
            self.som_carroca.play()
        elif text == 'Submarino':
            self.ids.mensagem.text= '[i][color=#FF3333]Até 82 km/h[/color][/i]'
            self.minha_imagem= 'submarino.jpg'
            self.som_submarino.play()
        elif text == 'Trem':
            self.ids.mensagem.text= '[i][color=#FF3333]Até 90 km/h[/color][/i]'
            self.minha_imagem= 'trem.jpg'
            self.som_trem.play()
        elif text == 'Triciclo':
            self.ids.mensagem.text= '[i][color=#FF3333]Até 100 km/h[/color][/i]'
            self.minha_imagem= 'triciclo.jpg'
            self.som_triciclo.play()
        elif text == 'Tuc Tuc':
            self.ids.mensagem.text= '[i][color=#FF3333]Até 70 km/h[/color][/i]'
            self.minha_imagem= 'tuctuc.jpg'
            self.som_tuctuc.play()

    def controla_som(self, situacao):
        if situacao:
            self.som_aeronave.volume  = 1
            self.som_carroca.volume   = 1
            self.som_submarino.volume = 1
            self.som_trem.volume      = 1
            self.som_triciclo.volume  = 1
            self.som_tuctuc.volume    = 1
            self.som_sair.volume      = 1
        else:
            self.som_aeronave.volume  = 0
            self.som_carroca.volume   = 0
            self.som_submarino.volume = 0
            self.som_trem.volume      = 0
            self.som_triciclo.volume  = 0
            self.som_tuctuc.volume    = 0
            self.som_sair.volume      = 0
            
    def sair(self):
        self.som_sair.play()
        Clock.schedule_once(self.encerrar,2)

    def encerrar(self,valor):
        App.get_running_app().stop()


class Meios_TransporteApp(App):
    def build(self):
        self.title= 'Meios de Transporte'
        return Principal()

transportes = Meios_TransporteApp()
transportes.run()
