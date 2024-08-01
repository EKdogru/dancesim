import socket
from tkinter import *
import tkinter.ttk as ttk

# UDP client ayarları
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_dance_command(dance_mode):
    message = dance_mode.encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))

def send_custom_command(command):
    message = command.encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))

pencere = Tk()
pencere.geometry("600x600+500+100")

pencere_basligi = "Buton Menü"
baslik = pencere.title(pencere_basligi)

etiket_metni = "Menü"
etiket = Label(text=etiket_metni, fg="white", bg="black", font=("Times", 25, "underline"))
etiket.pack(pady=(0, 10))

style = ttk.Style()
style.configure("Red.TButton", foreground="black", background="firebrick", font=("Times", 13, "bold"))

dugme1 = ttk.Button(pencere, text="Şarkı1", style="Red.TButton", command=lambda: send_dance_command('DansModu gangnam')) #ok
dugme1.pack(pady=(0, 10))

dugme2 = ttk.Button(pencere, text="Şarkı2", style="Red.TButton", command=lambda: send_dance_command('DansModu ankara')) #ok
dugme2.pack(pady=(0, 10))

dugme3 = ttk.Button(pencere, text="Şarkı3", style="Red.TButton", command=lambda: send_dance_command('DansModu floss')) #ok
dugme3.pack(pady=(0, 50))

dugme6 = Button(text="YeniKarekter", fg="white", bg="orange", font=("Times", 15, "bold"), command=lambda: send_custom_command('YeniKarekter')) #ok
dugme6.pack()

dugme8 = Button(text="Reset", fg="white", bg="magenta", font=("Times", 15, "bold"), command=lambda: send_custom_command('Reset')) #ok
dugme8.pack()

dugme5 = Button(text="FreeMod", fg="white", bg="blue", font=("Times", 15, "bold"), command=lambda: send_custom_command('FreeMode'))
dugme5.pack()

dugme7 = Button(text="Kasık",fg="white",bg="black",font=("Times",15,"bold"),command=lambda:send_custom_command('Kasik'))
dugme7.pack()

dugme9 = Button(text="Challange", fg="white",bg="purple", font=("Times",15,"bold"),command=lambda:send_custom_command('Challange'))
dugme9.pack()

dugme4 = Button(text="Stop", fg="white", bg="red", font=("Times", 20, "bold"), command=pencere.quit)
dugme4.pack()



pencere.mainloop()
