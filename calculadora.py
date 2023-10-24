import tkinter as tk

def add_values():
    value1 = float(entry1.get())
    value2 = float(entry2.get())
    value3 = float(entry3.get())
    value4 = float(entry4.get())
    value5 = float(entry5.get())
    value6 = float(entry6.get())
    
    result = value1 + value2 + value3 + value4 + value5 + value6
    result_text.delete(1.0, tk.END)  # Clear the text box
    result_text.insert(tk.END, f"Total: {result:.2f}")

# Create the main application window
root = tk.Tk()
root.title("Calculadora de valores")

# Create labels and entry fields
label1 = tk.Label(root, text="DMorais - Correção:")
label2 = tk.Label(root, text="DMorais - Juros:")
label3 = tk.Label(root, text="DMorais - Honorários:")
label4 = tk.Label(root, text="DMateriais - Correção:")
label5 = tk.Label(root, text="DMateriais - Juros:")
label6 = tk.Label(root, text="DMateriais - Honorários:")

label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

label4.grid(row=3, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1)

label5.grid(row=4, column=0)
entry5 = tk.Entry(root)
entry5.grid(row=4, column=1)

label6.grid(row=5, column=0)
entry6 = tk.Entry(root)
entry6.grid(row=5, column=1)

# Create the "Add" button
add_button = tk.Button(root, text="Add", command=add_values)
add_button.grid(row=6, columnspan=2)

# Create a text box to display the result
result_text = tk.Text(root, height=1, width=20)
result_text.grid(row=7, columnspan=2)

# Start the tkinter main loop
root.mainloop()