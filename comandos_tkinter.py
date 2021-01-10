from tkinter import *
from tkinter import ttk

def teste():
    print('Click')
    if edit1.get():
        label['text'] = edit1.get()
    else:
        label['text'] = 'Click do botao'

janela = Tk()

janela.title('Titulo da Janela')
janela.geometry('500x500')
janela.resizable(False,False)

'LABEL'
label = Label(janela, text='Label', bg='gray', fg='black', padx=2, pady=2)
label.grid(row=0, column=0,columnspan=2)

'EDIT TEXT'
edit1 = Entry(janela)
edit1.grid(row=1, column=0)

'BUTTON'
Button(janela, text='Botao', command=teste).grid(row=1, column=1)

tree = ttk.Treeview(janela, selectmode='browse', column=('column1','column2','column3'), show='headings')

tree.column('column1', width=150, minwidth=50, stretch=NO)
tree.heading("#1",text='Nome')
tree.column('column2', width=100, minwidth=50, stretch=NO)
tree.heading("#2",text='Idade')
tree.column('column3', width=200, minwidth=50, stretch=NO)
tree.heading("#3",text='Rua')

elementos = ['christian',36,'rua minas gerais']
tree.insert('',END,values=elementos)
tree.grid(row=2, column=0, columnspan=2)


janela.mainloop()
