from tkinter import *
root =Tk()
root.title("Password Strength Checker")
root.geometry("500x500")

title = Label(
    root,
    text="password strength checker",
    font=("Arial",18, "bold")
)
title.pack(pady=10)

password_label= Label(

    root,
    text=("Enter Your Password:")
)
password_label.pack()

password_entry =Entry(
    root,
    width=30,
    show="*"
)
password_entry.pack(pady=7)

result_label = Label(
    root,
    text=""
)
result_label.pack(pady=10)


import re
def check_password():
    password=password_entry.get()
    score = 0
    if len(password) >= 8:
        score=score+1
    else:
        print("Password should be atleast 8 characters long.")

    if re.search(r"[A-Z]",password):
        score = score+1
    else:
        print("Please include atleast one Uppercase Letter!")


    if re.search(r"[a-z]",password):
        score+= 1
    if re.search(r"[0-9]",password):
        score+=1
    if re.search(r"[@#$₹%^&*(){}|?/;:]", password):
            score+=1

    #determine the strength:
    if score<=2:
        result_label.config(
            text=f"Weak Password!({score}/5)"
        )

    elif score ==3:
        result_label.config(
            text=f"Moderate Password! Still easy to crack :) ({score}/5)"
        )
    elif score ==4:
            result_label.config(
                text=f"Good Password! Not that easy to crACK:) ({score}/5)"
            ) 
    elif score ==5:
            result_label.config(
                text=f"DIFFICULT! securing ur password....... :) ({score}/5)"
            )
#button
check_button =Button(
    root,
    text = "Check Strength",
    command =check_password
)
check_button.pack(pady=10)

root.mainloop()
