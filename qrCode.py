import qrcode
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from tkinter import filedialog

# Creating the window
wn = Tk()
wn.title('URL QR Code Generator')
wn.geometry('400x616')
wn.config(bg='white')
# wn.overrideredirect(True)

# Load Roboto font
font_bold = tkFont.Font(family="Roboto", size=13, weight="bold")
font_normal = tkFont.Font(family="Roboto", size=12)

# Creating a label to display the QR code
qr_label = Label(wn, bg="#2B7DFA")
qr_label.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.47)

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


# Label for the window
# Taking the input of the text or URL to get QR code
Frame1 = Frame(wn, bg="white")
Frame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

text_box1 = Entry(Frame1, highlightbackground="#2B7DFA",
                  highlightthickness=2, relief="groove", font=font_bold, fg="#747474")
text_box1.place(relx=0.005, rely=0.05, relwidth=0.99, relheight=0.6)

# Set a preview text
preview_text = "Insert link"
text_box1.insert(0, preview_text)

# Function to clear the text_box1 widget when clicked


def clear_text(event):
    text_box1.delete(0, END)


# Bind the clear_text function to the text_box1 widget
text_box1.bind("<Button-1>", clear_text)

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
