# Adım 1 Modülü Import Et!
from tkinter import *
from tkinter import messagebox
#Adım 6 import base64 encryption
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#Adım 5 Dosyaları Kaydetmek:

def save_and_encrypt_notes():
    title = my_title.get()
    message = input_text.get("1.0", END)
    my_master_key = my_key.get()

    if len(title) == 0 or len(message) == 0 or len(my_master_key) == 0:
        messagebox.showinfo(title="Error!",message="Please enter all info.")
# Bütün bu işlemlerden sonra save_and_encrypt_notes i button a atamaya git!
    else:
        #encryption SON ADIM!!!
        message_encrypted = encode(my_master_key, message)
        try:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            my_title.delete(0,END)
            my_key.delete(0,END)
            input_text.delete("1.0",END)

def decrypt_notes():
    message_encrypted = input_text.get("1.0", END)
    my_secretkey = my_key.get()

    if len(message_encrypted) == 0 or len(my_secretkey)== 0:
        messagebox.showinfo(title="Error!", message="Please enter all info!")
    else:
        try:
            decrypted_message = decode(my_secretkey,message_encrypted)
            input_text.delete("1.0", END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Error!", message="Please enter encrypted text!")

#Adım 1 importtan sonra window ismi genişliği falan basit işler bunlar :)
import tkinter
FONT = ("Verdena",15,"normal")
window = tkinter.Tk()
window.geometry("400x800")
window.title("Secret Data")
window.config(height=800, width=450)

#Adım 4 Yukarıya Görsel Oluştur!
my_batman_image = PhotoImage(file = "skull.png")
#my_batman_label = Label(image=my_batman_image)
#my_batman_label.pack()

#Image koymanın 2. Yolu:
canvas_batman = Canvas(height=200,width=200)
canvas_batman.create_image(100,100,image=my_batman_image)
canvas_batman.pack()

# Adım 2 Kullanıcıdan değer iste

my_title_label = tkinter.Label(text="Enter your title", font=FONT)
my_title_label.pack()
my_title = Entry(width=40)
my_title.pack()

my_secret_title_label = tkinter.Label(text="Enter your secret", font=FONT)
my_secret_title_label.pack()
input_text = Text(width=40,height=20)
input_text.pack()


my_master_key = tkinter.Label(text="Enter master key", font=FONT)
my_master_key.pack()
my_key = tkinter.Entry(width=40)
my_key.pack()


# Adım 3 Buton yarat!
# Buton 1
save_button = tkinter.Button(text="Save & Encrypt", width=15,command=save_and_encrypt_notes)
save_button.pack()
# Buton 2
decrypt_button = tkinter.Button(text="Decrypt", width=10,command=decrypt_notes)
decrypt_button.pack()

window.mainloop()
