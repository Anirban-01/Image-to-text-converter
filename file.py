from tkinter import filedialog
import pytesseract
import cv2
import tkinter as tk

# specify tesseract.exe file location
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

window = tk.Tk()
window.geometry('455x600')
window.resizable(False, False)
window.title('IMAGE TO TEXT CONVERTER')
window.configure(bg='#B0C4DE')

get_text = tk.StringVar()


# select_image function to select image from directory
def select_image():
    """Making image variable global"""
    global image
    """filedialog is used to select the image"""
    fileName = filedialog.askopenfilename(initialdir="/", title="Select a Image",
                                          filetype=(
                                              ('All Files', '*.*'), ("jpeg", "*.jpeg"), ("png", "*.png"),
                                              ('jpg', '*.jpg'),))

    """opencv library is used to read image from selected directory"""
    image = cv2.imread(fileName)
    scale_percent = 50  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dimensions = (width, height)
    # resize image
    image_resized = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
    cv2.imshow('resized', image_resized)


def extract_text():
    global extract_data
    extract_data = pytesseract.image_to_string(image)
    value = extract_data
    result = retrive_text.insert(tk.END, value)


retrive_text = tk.Text(window, height=15, width=40, bg='#f5f5f5', font='Arial')
retrive_text.grid(row=0, column=0, padx=5, pady=5)


def save_text():
    select_file_type = filedialog.asksaveasfilename(initialdir='/',
                                                    filetypes=[('text', '.txt'), ('pdf', '.pdf'), ('word', '.doc'),
                                                               ('excel', '.xls'), ('All Files', '*.*')],
                                                    defaultextension=".txt")

    with open(select_file_type, "w") as file:
        file.write(extract_data)
        file.close()


Show_image_button = tk.Button(window, text='Select Image', command=select_image, font=5, bg='#dcdcdc').grid(row=1,
                                                                                                            column=0,
                                                                                                            padx=10,
                                                                                                            pady=10)

Extract_text_button = tk.Button(window, text='Extract Text', command=extract_text, font=5, bg='#dcdcdc').grid(row=2,
                                                                                                              column=0,
                                                                                                              padx=10,
                                                                                                              pady=10)

Save_text_button = tk.Button(window, text='Save Text', command=save_text, font=5, bg='#dcdcdc').grid(row=3, column=0,
                                                                                                     padx=10, pady=10)

Exit_button = tk.Button(window, text='Exit', command=exit, font=5, bg='#dcdcdc').grid(row=4, column=0, padx=10, pady=10)

window.mainloop()
