import tkinter as tk
import numpy as np

root = tk.Tk()
# Defining the geometry of the app
root.geometry("400x450")
# Putting a car image as background of the app
img = tk.PhotoImage(file='Car1.png')
label = tk.Label(root, image=img)
label.place(x=-2, y=-2)
# Title of the app
title_label = tk.Label(root, text='Car Price Prediction System', font=('calibre', 10, 'bold'))
title_label.config(fg="#0000FF")
title_label.config(bg="yellow")
title_label.grid(row=0, column=0, padx=10, pady=10)

# Input parameters
present_price = tk.StringVar()
kms_driven = tk.StringVar()
Age = tk.StringVar()


# Submit function where the inputs are taken and then passed to the model
# that we created and displaying the results
def submit():
    # Input variables
    present_price_tag = present_price.get()
    kms_driven_tag = kms_driven.get()
    Age_tag = Age.get()
    Fuel_type_tag = clicked_fuel.get()
    seller_type_tag = clicked_seller.get()
    Transmission_tag = clicked_trans.get()
    Owner_tag = clicked_owner.get()

    # terminal output statements for our reference
    print("Present Price : " + present_price_tag)
    print("KMS Driven : " + kms_driven_tag)
    print("Age of the car : " + Age_tag)
    print("Fuel Type : " + Fuel_type_tag)
    print("Seller Type : " + seller_type_tag)
    print("Transmission Type : " + Transmission_tag)
    print("Owner Type : " + Owner_tag)

    # this is done because we did one hot encoding of our data in model creation to reduce the complexity of the model
    if Fuel_type_tag == "Petrol":
        Petrol = 1
        Diesel = 0
    elif Fuel_type_tag == "Diesel":
        Petrol = 0
        Diesel = 1
    else:
        Petrol = 0
        Diesel = 0

    if seller_type_tag == "Individual":
        s_type = 1
    else:
        s_type = 0

    if Transmission_tag == "Manual":
        t_type = 1
    else:
        t_type = 0

    if Owner_tag == "1st Hand":
        Owner = 0
    elif Owner_tag == "2nd Hand":
        Owner = 1
    else:
        Owner = 3

    # Loading the model
    import pickle
    global lrLangDetectionModel
    lrLangDetectionFile = open('random_forest_regression_model.pckl', 'rb')
    lrLangDetectionModel = pickle.load(lrLangDetectionFile)

    # Passing the input taken from input fields
    model_input = [present_price_tag, kms_driven_tag, Owner, Age_tag, Diesel, Petrol, s_type, t_type]
    pred = lrLangDetectionModel.predict([model_input])

    # prediction of the model
    output = pred[0]
    output = "{:.2f}".format(output)
    print('Predicted cost(selling price): ' + str(output))

    # Prediction/Selling price displaying in the app
    selling_price_label = tk.Label(root, text='Selling Price :', font=('calibre', 10, 'bold'))
    selling_price_label.grid(row=8, column=0, padx=10, pady=10)
    selling_price_label.config(fg="#0000FF")
    selling_price_label.config(bg="yellow")
    price = tk.Label(root, text=str(output) + ' Lakhs rupees', font=('calibre', 10, 'bold'))
    price.grid(row=8, column=1, padx=10, pady=10)

    # resetting the values for next cycle
    present_price.set("")
    kms_driven.set("")
    Age.set("")
    clicked_fuel.set("Petrol")
    clicked_seller.set("Dealer")
    clicked_trans.set("Manual")


# creating a label for
# Present Price using widget Label
present_price_label = tk.Label(root, text='Present Price (in Lakhs rupees)', font=('calibre', 10, 'bold'))
present_price_label.config(fg="#0000FF")
present_price_label.config(bg="yellow")
# creating a entry for input
# Present Price using widget Entry
PP_entry = tk.Entry(root, textvariable=present_price, font=('calibre', 10, 'normal'))

# creating a label for KMS
kms_label = tk.Label(root, text='KMS Driven (Kilometers)', font=('calibre', 10, 'bold'))
kms_label.config(fg="#0000FF")
kms_label.config(bg="yellow")
# creating a entry for KMS
kms_entry = tk.Entry(root, textvariable=kms_driven, font=('calibre', 10, 'normal'))

# creating a label for Age
Age_label = tk.Label(root, text='How old is the car (Years)', font=('calibre', 10, 'bold'))
Age_label.config(fg="#0000FF")
Age_label.config(bg="yellow")
# creating a entry for Age
Age_entry = tk.Entry(root, textvariable=Age, font=('calibre', 10, 'normal'))

# creating a label for Fuel Type
Fuel_type_label = tk.Label(root, text='Fuel_type', font=('calibre', 10, 'bold'))
Fuel_type_label.config(fg="#0000FF")
Fuel_type_label.config(bg="yellow")
# creating a entry for Fuel Type

options_fuel = ["Petrol", "Diesel", "CNG"]
clicked_fuel = tk.StringVar()
clicked_fuel.set("Petrol")
Fuel_type_entry = tk.OptionMenu(root, clicked_fuel, *options_fuel)

# creating a label for seller type
seller_type_label = tk.Label(root, text='Seller Type', font=('calibre', 10, 'bold'))
seller_type_label.config(fg="#0000FF")
seller_type_label.config(bg="yellow")
# creating a entry for seller type
options_seller = ["Dealer", "Indiviual"]
clicked_seller = tk.StringVar()
clicked_seller.set("Dealer")
seller_type_entry = tk.OptionMenu(root, clicked_seller, *options_seller)

# creating a label for trans type
Transmission_label = tk.Label(root, text='Transmission Type', font=('calibre', 10, 'bold'))
Transmission_label.config(fg="#0000FF")
Transmission_label.config(bg="yellow")
# creating a entry for trans type
options_trans = ["Manual", "Auto"]
clicked_trans = tk.StringVar()
clicked_trans.set("Manual")
trans_type_entry = tk.OptionMenu(root, clicked_trans, *options_trans)

# creating a label for trans type
owner_label = tk.Label(root, text='Owner', font=('calibre', 10, 'bold'))
owner_label.config(fg="#0000FF")
owner_label.config(bg="yellow")
# creating a entry for trans type
options_owner = ["1st Hand", "2nd Hand", "3rd Hand"]
clicked_owner = tk.StringVar()
clicked_owner.set("1st Hand")
owner_entry = tk.OptionMenu(root, clicked_owner, *options_owner)

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
present_price_label.grid(row=1, column=0, padx=10, pady=10)
PP_entry.grid(row=1, column=1, padx=10, pady=10)
kms_label.grid(row=2, column=0, padx=10, pady=10)
kms_entry.grid(row=2, column=1, padx=10, pady=10)
Age_label.grid(row=3, column=0, padx=10, pady=10)
Age_entry.grid(row=3, column=1, padx=10, pady=10)
seller_type_label.grid(row=4, column=0, padx=10, pady=10)
seller_type_entry.grid(row=4, column=1, padx=10, pady=10)
Fuel_type_label.grid(row=5, column=0, padx=10, pady=10)
Fuel_type_entry.grid(row=5, column=1, padx=10, pady=10)
Transmission_label.grid(row=6, column=0, padx=10, pady=10)
trans_type_entry.grid(row=6, column=1, padx=10, pady=10)
owner_label.grid(row=7, column=0, padx=10, pady=10)
owner_entry.grid(row=7, column=1, padx=10, pady=10)
sub_btn.grid(row=9, column=1, padx=10, pady=10)

# performing an infinite loop
# for the window to display
root.mainloop()
