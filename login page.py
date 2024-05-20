from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title("Login")
root.geometry("900x450+300+100")
root.resizable(False, False)
root.configure(bg="white")
# f5f8f8

#############################################################################################
def signup_command():
    window=Toplevel(root)
    window.title("Sign Up")
    window.geometry("900x450+300+100")
    window.resizable(False, False)
    window.configure(bg="white") #f5f8f8

    def signup():
        username=Name.get()
        code=password.get()
        confirm_password=confirm_code.get()

        if code==confirm_password:
            try:
                file=open("datasheet.txt", 'r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:code}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt', 'w')
                w=file.write(str(r))

                messagebox.showinfo("Sign up", "Successfully sign up")
                window.destroy()

            except:
                file=open('datasheet.txt', 'w')
                pp=str({"username":"code"})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror("Invalid", "Both passwords should match")

    def sign():
        window.destroy()
        
    
        
        
    #icon
    '''image_icon=PhotoImage(file="Images/icon.png")
    root.iconphoto(False, image_icon)'''


    img = PhotoImage(file="signup.png")
    top_image=Label(window,image=img,background="white")
    top_image.place(x=50,y=90) # x=10

    frame = Frame(window,width=350,height=390, bg="#57a1f8")
    frame.place(x=480,y=50)


    heading=Label(frame, text="Sign up", fg="#fff",bg="#57a1f8", font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100,y=5)

    #Entry box
    def on_enter(e):
        Name.delete(0, 'end')

    def on_leave(e):
        name=Name.get()
        if name=='':
            Name.insert(0, 'Username')
        


    Name = Entry(frame,width=25, font=('Microsoft YaHei UI Light', 11), bg="#57a1f8", fg="#000", bd=0)
    Name.place(x=30, y=80)
    Name.insert(0, 'Username')
    Name.bind("<FocusIn>", on_enter)
    Name.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2, bg="black").place(x=25,y=107) # to draw line


    def on_enter(e):
        password.delete(0, 'end')

    def on_leave(e):
        name=password.get()
        if name=='':
            password.insert(0, 'Password')
        

    password = Entry(frame,width=25, font=('Microsoft YaHei UI Light', 11), bg="#57a1f8", fg="#000", bd=0)
    password.place(x=30, y=150)
    password.insert(0, 'Password')
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2, bg="black").place(x=25,y=177) # to draw line

    def on_enter(e):
        confirm_code.delete(0, 'end')

    def on_leave(e):
        name=confirm_code.get()
        if name=='':
            confirm_code.insert(0, 'Confirm password')
        

    confirm_code = Entry(frame,width=25, font=('Microsoft YaHei UI Light', 11), bg="#57a1f8", fg="#000", bd=0)
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm password')
    confirm_code.bind("<FocusIn>", on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2, bg="black").place(x=25,y=247) # to draw line


    Button(frame,text="Sign Up", bd=0,pady=7,width=39,bg="#fff", fg="black", command=signup).place(x=35,y=280)
    label =Label(frame, text="I have an account?", font=('Microsoft YaHei UI Light', 9), bg="#57a1f8", fg="#000")
    label.place(x=90, y=340)

    sign_in = Button(frame,text="Sign in", bd=0,pady=7,width=6,fg="white", bg="#57a1f8", cursor='hand2', command=sign)
    sign_in.place(x=200,y=340)

    window.mainloop()
    
################################################################################################################################
def signin():
    username = Name.get()
    code = password.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r=ast.literal_eval(d)
    file.close()

##    print(r.keys())
##    print(r.values())
    
    if username in r.keys() and code == r[username]:
        print("Benedict now knows how to code")
        screen = Toplevel()
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        lbl = Label(screen, text="Benedict now knows how to code", bg="white", font=("calibre(body)", 20, "bold"))
        lbl.pack(expand=True)
        screen.mainloop()
    else:
        messagebox.showerror("Invalid", "Invalid username or password!!")


# icon
'''image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)'''


img = PhotoImage(file="login.png")
top_img = Label(root, image=img, background="white")
top_img.place(x=50, y=50)
# x=10

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=50)


heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Entry box


def on_enter(e):
    Name.delete(0, 'end')


def on_leave(e):
    name = Name.get()
    if name == '':
        Name.insert(0, 'Username')
        

Name = Entry(frame, width=25, font=('Microsoft YaHei UI Light', 11), bg="#ffffff", fg="#000", bd=0)
Name.place(x=30, y=80)
Name.insert(0, 'Username')
Name.bind("<FocusIn>", on_enter)
Name.bind("<FocusOut>", on_leave)

# to draw line
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


def on_enter(e):
    password.delete(0, 'end')


def on_leave(e):
    name = password.get()
    if name == '':
        password.insert(0, 'Password')
        

password = Entry(frame, width=25, font=('Microsoft YaHei UI Light', 11), bg="#ffffff", fg="#000", bd=0)
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)

# to draw line
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, text="Sign in", bd=0, pady=7, width=39, bg="#57a1f8", fg="white", command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", font=('Microsoft YaHei UI Light', 9), bg="white", fg="#000")
label.place(x=75, y=270)

sign_up = Button(frame, text="Sign up", bd=0, pady=7, width=6, fg="#57a1f8", bg="white", cursor='hand2', command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()
