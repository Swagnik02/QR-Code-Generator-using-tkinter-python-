import qrcode
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from tkinter import filedialog
import pyautogui as pg

# Creating the window
wn = Tk()
wn.title('URL QR Code Generator')
wn.geometry('400x616')
wn.config(bg='white')
wn.overrideredirect(True)

# Load Roboto font
font_bold = tkFont.Font(family="Roboto", size=13, weight="bold")
font_normal = tkFont.Font(family="Roboto", size=12)

# Placing the window in the center of the screen
def place_center(): 
    global x, y
    reso = pg.size()
    rx = reso[0]
    ry = reso[1]

    # To place in the middle 
    # x = int((rx/2) - (350/2))   #increase the value to move left
    # y = int((ry/2) - (800/2))   #increase the value to move up

    # To place in the right top corner
    x = int((rx) - (500))
    y = int((ry/2) - (900/2))


    wn.geometry(f"400x616+{x}+{y}")
place_center()

# Function to move the window
def move_window(event):
    wn.geometry(f'+{event.x_root}+{event.y_root}')

# Binding the events to the window
# wn.bind('<Button-1>', move_window)
# wn.bind('<B1-Motion>', move_window)

# Function to generate the QR code and display it
def generateCode():
    # print(text_box1.get())
    # Creating a QRCode object of the size specified by the user
    qr = qrcode.QRCode(version=4, box_size=10, border=3)

    # Adding the data to be encoded to the QRCode object
    qr.add_data(text_box1.get())

    qr.make(fit=True)  # Making the entire QR Code space utilized
    # Generating the QR Code
    img = qr.make_image(fill_color="white", back_color="transparent")

    # Display the QR code image in the label
    img = img.resize((200, 200))  # resize the QR code image
    qr_code = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_code)
    qr_label.image = qr_code

    return img

# Function to save the QR code
def saveCode():
    # Generating the QR code using the generateCode function
    img = generateCode()

    # Extracting the default name for saving from the URL
    url = text_box1.get()
    if url.startswith("https://www."):
        default_name = url.split('://www')[1].split('.')[0] + '.png'

    elif url.startswith("https://"):
        default_name = url.split('://')[1].split('.')[0] + '.png'

    else:
        default_name = url.split('.')[0] + '.png'

    # Ask the user to choose the save location and name for the QR code image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=default_name, filetypes=[("PNG", ".png")])

    # If the user cancels the save operation, do nothing
    if not file_path:
        return

    # Save the image to the chosen location and name
    img.save(file_path)
# Function to clear the text_box1 widget when clicked
def clear_text(event):
    text_box1.delete(0, END)

# Function to exit the window
def exit_window():
    wn.destroy()

# FrontEnd
# Button to quit
button_exit = Button(wn, text='X', relief="groove", font=(
    font_normal, 10), bg="#2B7DFA", fg="white", command=exit_window, bd=0)
button_exit.place(relx=0.9, rely=0, relwidth=0.1, relheight=0.068)

# Label for Heading
txt_label = Label(wn, text="QR CODE GENERATOR", font=(
    font_normal, 15), bg="#2B7DFA", fg="white")
txt_label.place(relx=0.1, rely=0.08, relwidth=0.8, relheight=0.068)

# INPUT_BOX
# Taking the input of the text or URL to get QR code
Frame1 = Frame(wn, bg="white")
Frame1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.11)

text_box1 = Entry(Frame1, highlightbackground="#2B7DFA",
                  highlightthickness=2, relief="groove", font=font_bold, fg="#747474")
text_box1.place(relx=0.005, rely=0.15, relwidth=0.99, relheight=0.6)

# Set a preview text
preview_text = "Insert link"
text_box1.insert(0, preview_text)

# Bind the clear_text function to the text_box1 widget
text_box1.bind("<Button-1>", clear_text)

# Creating a label to display the QR code
qr_label = Label(wn, bg="#2B7DFA")
qr_label.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.47)

# BUTTONS
# Button to generate the QR Code
button = Button(wn, text='EMBED', relief="groove", font=(
    font_normal, 10), bg="white", fg="#2B7DFA", command=generateCode, bd=0)
button.place(relx=0.1, rely=0.76, relwidth=0.8, relheight=0.065)

# Button to save the QR Code
button_save = Button(wn, text='EXPORT', relief="groove", font=(
    font_normal, 10), bg="#2B7DFA", fg="white", command=saveCode, bd=0)
button_save.place(relx=0.1, rely=0.84, relwidth=0.8, relheight=0.065)

# Runs the window till it is closed manually
wn.mainloop()
