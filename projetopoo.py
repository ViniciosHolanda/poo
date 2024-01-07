from tkinter import *
import pickle


class Aluguel:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('790x400')
        self.janela.title('Controle de Aluguel de Carros')

        self.canvas1 = Canvas(self.janela, width=790, height=400)
        self.canvas1.pack()

        self.titulo1 = Label(
            self.canvas1,
            text='Aluguel de Carro🚗🚗',
            width=52,
            height=2,
            bg='black',
            font='Arial 20 bold',
            fg='white',
            borderwidth=5,
            relief='flat',
        )
        self.titulo1.place(x=0,y=0)

        self.canvas1.create_line(
            550,50,
            550,600,
            dash = (5,2)
        )

        self.tituloLeitura = Label(
            self.canvas1,
            width=24,
            fg='blue',
            text='Dados do Adquirinte',
            bg='white',
            font='Helvetica 12'
        )
        self.tituloLeitura.place(x=560,y=80)

        self.textoNome1 = Label(
            self.canvas1,
            text='Nome: ',
            font='Helvetica 15'
        )

        self.textoNome1.place(x=560,y=110)

        self.textoNome3 = Label(
            self.canvas1,
            text='Telefone: ',
            font='Helvetica 15'
        )
        self.textoNome3.place(x=560,y=190)

        self.nomeArq1 = Entry(
            self.canvas1,
            width=21,
            font='Helvetica 14'
        )
        self.nomeArq1.place(x=560,y=140)

        self.telefoneArq1 = Entry(
            self.canvas1,
            width=21,
            font='Helvetica 14',
            
        )
        self.telefoneArq1.place(x=560,y=220)

        self.textoNome2 = Label(
            self.canvas1,
            text='N° do Carro: ',
            font='Helvetica 15'
        )
        self.textoNome2.place(x=560,y=270)

        self.nomeArq2 = Entry(
            self.canvas1,
            width=21,
            font='Helvetica 14'
        )
        self.nomeArq2.place(x=560,y=300)

        self.botaoGravar = Button(
            self.canvas1,
            width=20,
            text='Registrar Aluguel',
            bg='red',
            fg='white',
            font='Helvetica 14',
            command= self.apagarconteudo
        )
        self.botaoGravar.place(x=560,y=350)

        self.imagemcarro1 = PhotoImage(file="POO/carro1.png").subsample(6)
        self.img1 = self.canvas1.create_image(80, 120, image = self.imagemcarro1)
        self.car1 = Label(
            self.canvas1,
            width=24,
            fg='black',
            text='1',
            font='Helvetica 12')
        self.car1.place(x=-40,y=160)

        self.imagemcarro2 = PhotoImage(file="POO/carro2.png").subsample(3)
        self.img2 = self.canvas1.create_image(215, 120, image = self.imagemcarro2)
        self.car2 = Label(
            self.canvas1,
            width=24,
            fg='black',
            text='2',
            font='Helvetica 12')
        self.car2.place(x=90,y=160)

        self.imagemcarro3 = PhotoImage(file="POO/carro3.png").subsample(4)
        self.img3 = self.canvas1.create_image(350, 120, image = self.imagemcarro3)
        self.car3 = Label(
            self.canvas1,
            width=24,
            fg='black',
            text='3',
            font='Helvetica 12')
        self.car3.place(x=230,y=160)

        self.imagemcarro4 = PhotoImage(file="POO/carro4.png").subsample(3)
        self.img4 = self.canvas1.create_image(480, 120, image = self.imagemcarro4)
        self.car4 = Label(
            self.canvas1,
            width=20,
            fg='black',
            text='4',
            font='Helvetica 12')
        self.car4.place(x=360,y=160)

        self.imagemcarro5 = PhotoImage(file="POO/carro5.png").subsample(4)
        self.img5 = self.canvas1.create_image(80, 290, image = self.imagemcarro5)
        self.car5 = Label(
            self.canvas1,
            width=24,
            fg='black',
            text='5',
            font='Helvetica 12')
        self.car5.place(x=-40,y=340)

        self.imagemcarro6 = PhotoImage(file="POO/carro6.png").subsample(4)
        self.img6 = self.canvas1.create_image(215, 290, image = self.imagemcarro6)
        self.car6 = Label(
            self.canvas1,
            width=24,
            fg='black',
            text='6',
            font='Helvetica 12')
        self.car6.place(x=90,y=340)

        self.imagemcarro7 = PhotoImage(file="POO/carro7.png").subsample(2)
        self.img7 = self.canvas1.create_image(350, 290, image = self.imagemcarro7)
        self.car7 = Label(
            self.canvas1,
            width=24,
            fg='black',
            text='7',
            font='Helvetica 12')
        self.car7.place(x=230,y=340)

        self.imagemcarro8 = PhotoImage(file="POO/carro8.png").subsample(6)
        self.img8 = self.canvas1.create_image(480, 290, image = self.imagemcarro8)
        self.car8 = Label(
            self.canvas1,
            width=20,
            fg='black',
            text='8',
            font='Helvetica 12')
        self.car8.place(x=360,y=340)

        self.DadosDosContatos = {}

        self.janela.mainloop()

    def apagarconteudo(self):
        self.telefoneArq1.delete(0,END)
        self.nomeArq1.delete(0,END)
        self.nomeArq2.delete(0,END)

alugel = Aluguel()