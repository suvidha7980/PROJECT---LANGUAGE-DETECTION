#...........................................PROJECT - LANGUAGE DETECTION...............................................#

# import * represents all the functions and built-in modules in the tkinter library.
from tkinter import *

# To detect the language of the text we use langdetect which supports 55 languages.
# For this we need to install langdetect using $ pip install langdetect.
from langdetect import detect

# langcodes standardizes codes that refer to them, such as en for English, es for Spanish and hi for Hindi.
# For standardizing codes we need to install langcodes using $ pip install langcodes[data].
from langcodes import *


root = Tk()
root.title("Language Detection!")

root.geometry("500x400")
root.config(bg="gray90")


# Whenever Clear button gets clicked everything from the textbox will be erased.
def clearAll():
    my_text.delete(1.0, END)


# Whenever check language button gets clicked we will run a code.
def check_lang():

    # if statement is used to check whether there is sth in textbox and if not then simply pass the required message
    # 1.0 is the first position in the text box
    # end-1c means the position is one character ahead of "end"
    if my_text.compare("end-1c", "==", "1.0"):

        #  this means that there is nothing in the textbox
        my_label.config(text="Hey! you forget to enter anything...")

    else:

        # We will grab the language code i.e. detect and will detect everything from the textbox.
        code = detect(my_text.get(1.0, END))

        # Taking new variable to display language in label in standardized form.
        my_result = Language.make(language=code).display_name()

        # Passing message to be displayed in the label.
        my_label.config(text=f"Your Language Is: {my_result} ", fg="firebrick4")



my_text = Text(root, height=10, width=50)
#The pack() method is used to make a widget fill the entire frame
my_text.pack(pady=20)

my_button = Button(root, text="Check language", bg="darkslategray4", fg="white", height=1, width=20, command=check_lang)
my_button.pack(pady=20)

my_label = Label(root, text="Language Detected Is : ", font=15, bg="mistyrose3")
my_label.pack(pady=20)

button2 = Button(root, text="Clear", bg="darkorchid2", fg="white", height=5, width=10, command=clearAll)
button2.pack(pady=20)


# mainloop() method listens for events such as button clicks  & tells Python to run the Tkinter event loop.
root.mainloop()