from tkinter import *
from tkinter import messagebox
import random
import time


# game logic
game = ['ROCK', 'PAPER', 'SCISSOR']


def comp_select():
    global comp_selection
    number = [0, 1, 2]
    comp_choice = random.choice(number)
    comp_selection = game[comp_choice]


def user_selection(u):
    global player_selection
    player_selection = game[u]


# Score for final result
comp_score = 0
player_score = 0


def winning():
    global comp_score
    global player_score
    if player_selection == comp_selection:
        info1['text'] = 'Its a Tie'

    if player_selection == 'ROCK' and comp_selection == "SCISSOR":
        info1['text'] = 'PLAYER WINS....'
        player_score += 1
    if player_selection == 'PAPER' and comp_selection == "SCISSOR":
        info1['text'] = '  COMPUTER WINS....'
        comp_score += 1

    if player_selection == 'ROCK' and comp_selection == "PAPER":
        info1['text'] = '  COMPUTER WINS....'
        comp_score += 1
    if player_selection == 'SCISSOR' and comp_selection == "PAPER":
        info1['text'] = 'PLAYER WINS....'
        player_score += 1

    if player_selection == 'SCISSOR' and comp_selection == "ROCK":
        info1['text'] = '  COMPUTER WINS....'
        comp_score += 1
    if player_selection == 'PAPER' and comp_selection == "ROCK":
        info1['text'] = 'PLAYER WINS....'
        player_score += 1


root = Tk()
r1 = root
root.title('Rock,Paper & Scissor')
root.iconbitmap(r"resource\icon1.ico")

# creating menubar
menubar = Menu(root)
root.config(menu=menubar)

# .............creating submenu...........

# define function for about us menu


def about_us():
    about = Toplevel(root)
    about.title('About Us')
    about.iconbitmap(r"resource\icon1.ico")

    about_msg = Label(
        about, text='''This is a simple game build using Python Tkinter
     by @kmvishu and @sreyaz''')
    about_msg.config(font=("Fira", 15))
    about_msg.pack()

    about_icon = PhotoImage(
        file=r'resource\about_us.png')
    about_label = Label(about, image=about_icon)
    about_label.image = about_icon  # keeping refrence to not destroy by python garbage collection
    about_label.pack()

    statusbar = Label(about, text='About Rock,Paper and Scissor',
                      bd=1, relief=SUNKEN, anchor=W)
    statusbar.pack(side=BOTTOM, fill=X, anchor=W)

# define function for about us menu


def rules():
    rule = Toplevel(root)
    rule.title('Rules')
    rule.iconbitmap(r"resource\icon1.ico")

    page = Label(rule, text='Here are the rules for games:\n'
                 + "Rock vs Paper->Paper Wins \n"
                 + "Rock vs Scissor->Rock Wins \n"
                 + "Paper vs Scissor->Scissor Wins \n")
    page.config(font=("Fira", 15))
    page.pack(padx=12, pady=12)

    about_icon = PhotoImage(
        file=r'resource\about_us.png')
    page_logo = Label(rule, image=about_icon)
    page_logo.image = about_icon
    page_logo.pack()

    statusbar = Label(rule, text='Rules For Game', bd=1, relief=SUNKEN, anchor=W)
    statusbar.pack(side=BOTTOM, fill=X, anchor=W)


# menu creation
def submenu_creation():
    submenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=submenu)
    submenu.add_command(label='Rules', command=rules)
    submenu.add_command(label='About Us', command=about_us)


submenu_creation()

# welcom screen creation
welcome = Label(root, text='Welcome To Rock,Paper and Scissor Game',)
welcome.config(font=("Fira", 20))
welcome.pack(padx=12, pady=12)


# creating computer thinking Popoup
def comp_thinking():
    global info1
    thinking_popup = Toplevel(game_window)
    thinking_popup.iconbitmap(
        r"resource\icon1.ico")
    comp_info = Label(thinking_popup, text='Please wait Computer is thinking.......')
    comp_info.config(font=('Fira', 20))
    comp_info.pack()
    # TODO: add gif on tiknter
    photo = PhotoImage(
        file=r'resource\think\frame_000_delay-0.02s.gif')
    think = Label(thinking_popup, image=photo)
    think.image = photo
    think.pack()
    thinking_popup.after(2000, lambda: thinking_popup.destroy()
                         )  # Destroy the widget after 2 seconds

    # TODO: reset label everytime when rado button is pressed

    time.sleep(3)
    comp_select()
    user_selection(v.get())
    info1 = Label(choice_frame, text='Your Choice is.....'+player_selection)
    info1.config(font=('Fira', 20))
    info1.grid(row=5)
    info2 = Label(choice_frame, text='Computer Choice is.....'+comp_selection)
    info2.config(font=('Fira', 20))
    info2.grid(row=6)
    time.sleep(5)
    winning()


# selection and greeting function


def submit():
    global v

    # greetings
    if name.get():
        if name.get().isalpha():
            sorted
            final_name = name.get().title()
            name.delete(0, END)  # clear input field after taking input from user
            hello = Label(choice_frame, text='Hello!! '+final_name)
            hello.config(font=("Fira", 14))
            hello.grid(row=0)
            choice_label = Label(choice_frame, text="Please choose your option")
            choice_label.config(font=("Fira", 14))
            choice_label.grid(row=1)

            # Radio button for taking input from user
            v = IntVar()
            rock_button = Radiobutton(choice_frame, text='Rock', command=comp_thinking, relief='raised',
                                      padx=2, borderwidth=2, variable=v, value=0)
            rock_button.config(font=('Fira', 13))
            rock_button.grid(row=2, pady=4)
            paper_button = Radiobutton(choice_frame, text="Paper", command=comp_thinking, relief='raised',
                                       padx=2, borderwidth=2, variable=v, value=1)
            paper_button.config(font=('Fira', 13))
            paper_button.grid(row=3, pady=4)
            scissor_button = Radiobutton(choice_frame, text='Scissor', command=comp_thinking, relief='raised',
                                         padx=2, borderwidth=2, variable=v, value=2)
            scissor_button.config(font=('Fira', 13))
            scissor_button.grid(row=4, pady=4)
        else:
            error_box = messagebox.showerror('Error', "Name Can not be Numeric")

    else:
        error_box = messagebox.showerror('Error', 'Please Input Your Name First')


# creation of game game_window


def proceed():
    global game_window
    global choice_frame
    global submit_b1
    global name
    global submenu_creation
    global name_check

    # game window creation
    game_window = Toplevel(root)
    game_window.geometry('375x370')
    game_window.iconbitmap(r"resource\icon1.ico")  # TODO : causing error for minimizing window

    # menubar in game window ## TODO: error while creating menubar menubar not creating
    menubar = Menu(game_window)
    game_window.config(menu=menubar)
    submenu_creation()

    name_label = Label(game_window, text="Please Enter Your Name Below")
    name_label.config(font=('Fira', 14))
    name_label.pack()

    # Entry box creation
    name = Entry(game_window, width=20, font="Fira")
    name.pack(pady=2, ipady=4)

    # submit button creation
    submit_image = PhotoImage(
        file=r'C:resource\submit.png')
    submit_b1 = Button(game_window, image=submit_image, bd=0, command=submit)
    submit_b1.image = submit_image
    submit_b1.pack()

    # game window statusbar
    g_statusbar = Label(game_window, text="Let's Start.....", bd=1, relief=SUNKEN, anchor=W)
    g_statusbar.pack(side=BOTTOM, fill=X, anchor=W)

    # a frame creation
    choice_frame = Frame(game_window)
    choice_frame.pack()
    root.withdraw()


# proceed button creation on root  screen
enter_image = PhotoImage(
    file=r'resource\proceed.png')
proceed = Button(root, image=enter_image, command=proceed, bd=0)
proceed.pack(padx=12, pady=7)

# creating statusbar on root screen
statusbar = Label(root, text='Welcome to Rock,Paper and Scissor',
                  bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X, anchor=W)


root.mainloop()
