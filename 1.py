import tkinter as tk
from tkinter import messagebox

def calculate_body_fat(weight, height, gender, age):
    try:
        weight = float(weight)
        height = float(height)/100
        age = int(age)
    except ValueError:
        messagebox.showerror('Incorrerct','Please enter the right value')
        return
    
    bmi = weight / (height ** 2)
    
    if gender == 'male':
        body_fat = 1.20 * bmi + 0.23 * age - 16.2
    else:
        body_fat = 1.20 * bmi + 0.23 * age - 5.4
        
    messagebox.showinfo('Calculate Result', f'Your body fatness is:{body_fat:.2f}%')
    
root = tk.Tk()
root.title('Body fatness Calculator')
root.geometry('300x400')

label_title = tk.Label(root, text='Body fatness calculator', font=('English',16))
label_title.pack(pady=10)

label_weight = tk.Label(root, text='Enter your weight(kg):')
label_weight.pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

label_height = tk.Label(root, text='Enter your height(cm):')
label_height.pack()
entry_height = tk.Entry(root)
entry_height.pack()

label_gender = tk.Label(root, text='Select your gender:')
label_gender.pack()

gender_var = tk.StringVar(value='male')
radio_male = tk.Radiobutton(root, text='male', variable=gender_var, value='male')
radio_female = tk.Radiobutton(root, text='female', variable=gender_var, value='female')
radio_female.pack()
radio_male.pack()

label_age = tk.Label(root, text='Enter your age:')
label_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()

def on_calculator():
    weight = entry_weight.get()
    height = entry_height.get()
    gender = gender_var.get()
    age = entry_age.get()
    calculate_body_fat(weight, height, gender, age)

btn_calculate  = tk.Button(root, text='Calculate Body Fatness', command=on_calculator)
btn_calculate.pack(pady=20)

root.mainloop()