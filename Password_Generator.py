import random

from tkinter import *

from tkinter import messagebox


def passw():

    alpha1 = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    alpha2 = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    alpha3 = ["0","1","2","3","4","5","6","7","8","9"]
    alpha4 = ["!","@","#","$","%","-","_","&"]

    alpha = alpha1 + alpha2 + alpha3 + alpha4

    num = entry.get()

    if num.isdigit() != True:
        messagebox.showerror("Error", "Please enter a number")
    else:
        
        Num = int(num)

        long = Num

        x = random.choices(alpha , k=long)

        password = "".join(x)

        messagebox.showinfo("Passwors_Generator" , "You'r password is : {}".format(password))

# ====================================================================================

tk = Tk()

tk.title("Password Generator")

#======================================================================================

width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()

middle_width = width //2 - 400//2
middle_hight = height//2 - 400//2

tk.geometry(f"400x400+{middle_width}+{middle_hight}")


tk.config(background="#022f43")

#=====================================================================================

frame = Frame(tk , bg="#022f43")

label = Label(frame , text="Password Generator" , font=("Tahoma" , 24 ) , foreground="#0688c2" , background="#022f43" )
label.pack()


label2 = Label(frame , text="Make yourself the strongest password !" , font=("Tahoma" , 15) , foreground="#0688c2" , background="#022f43")
label2.pack()


entry = Entry(frame , font=("roboto" , 15) , foreground="Black" , background="white" , relief="solid" )
entry.pack(pady=6)


button = Button(frame , text="Generator" ,  font=("roboto" , 15 ) , background="#066b97" , cursor="hand2" , command=passw)
button.pack(pady=6)

frame.pack(expand=YES)




tk.mainloop()
