from tkinter import *
window = Tk()
window.geometry("234x275")
Label(window, text = "Programa de Tradução DNA e RNA").pack()
window.title("BIOLOGIA")
def btn_click(item):
    global expression
    expression = expression + item
    input_text.set(expression)
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
def btn_equal():
    global expression
    fita=[]
    texto=""
    resp=[]
    cotons = {'UUU': 'phe', 'UUC':'phe', 'UUA': 'leu', 'UUG': 'leu', 'CUU':'leu','CUC':'leu','CUA':'leu','UCU':'ser','UCC':'ser',
              'UCA':'ser','UCG':'ser','CCU':'pro', 'CCC':'pro', 'CCA':'pro','CCG':'pro','ACU':'thr','CUG':'leu','AUU':'ile','AUC':'ile',
              'ACC':'thr','ACA':'thr','ACG':'thr','GCU':'ala','GCC':'ala','GCA':'ala','GCG':'ala', 'AUA':'ile',
              'UAU':'tyr','UAC':'tyr','UAA':'parada','UAG':'parada','CAU':'his','CAC':'his','CAA':'gln','AUG':'met',
              'CAG':'gln','AAU':'asn','AAC':'asn','AAA':'lys','AAG':'lys','GAU':'asp', 'GUU':'val','GUC':'val','GUA':'val','GUG':'val',
              'GAC':'asp','GAA':'glu','GAG':'glu','UGU':'cys','UGC':'cys','UGA':'parada','UGG':'trp',
              'CGU':'arg','CGC':'arg','CGA':'arg','CGG':'arg','AGU':'ser','AGC':'ser','AGA':'arg','AGG':'arg',
              'GGU':'gly','GGC':'gly','GGA':'gly','GGG':'gly'}
    for x in range(len(expression)):
        if expression[x]=='A':
            fita.append('U')
        if expression[x]=='C':
            fita.append('G')
        if expression[x]=='T':
            texto = 'Esse é um trecho de uma fita de DNA'
            fita.append('A')
        if expression[x]=='G':
            fita.append('C')
        if expression[x]=='U':
            texto = 'Esse é um trecho de uma fita de RNA'
            fita.append('A')
        if len(fita)%3==0 and 'U' not in expression:
            temp2 = fita[x-2],fita[x-1],fita[x]
            temp = ''.join([str(elem) for elem in temp2])
            for y in cotons:
                if y==temp:
                    resp.append(cotons[y])
    classificacao.set(texto)
    nomes.set('-'.join([str(index) for index in resp]))
    input_text.set(''.join([str(elem) for elem in fita]))
    expression = ""
expression = ""
nomes = StringVar()
classificacao=StringVar()
input_text = StringVar() #entrada
input_frame = Frame(window, width = 5, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 70, bg = "#eee", bd = 0, justify = CENTER)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # 'ipady' is an internal padding to increase the height of input field
btns_frame = Frame(window, bg = "gray")
btns_frame.pack()
clear = Button(btns_frame, text = "Limpar", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 1, column = 0, padx = 1, pady = 1)
equal = Button(btns_frame, text = "Calcular", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 1, column = 1, padx = 1, pady = 1)
a = Button(btns_frame, text = "A", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click('A')).grid(row = 2, column = 0, padx = 1, pady = 1)
t = Button(btns_frame, text = "T", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click('T')).grid(row = 2, column = 1, padx = 1, pady = 1)
c = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click('C')).grid(row = 2, column = 2, padx = 1, pady = 1)
g = Button(btns_frame, text = "G", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click('G')).grid(row = 3, column = 1, padx = 1, pady = 1)
u = Button(btns_frame, text = "U", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click('U')).grid(row = 3, column = 2, padx = 1, pady = 1)
Label(window, textvariable = classificacao).pack()
Label(window, textvariable = nomes).pack()
window.mainloop()
