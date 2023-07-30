import tkinter as tk

def show_results():
    with open("results.txt", "r") as file:
        results = file.read()
    root = tk.Tk()
    root.title("Currency Converter Results")
    text_widget = tk.Text(root, wrap="word")
    text_widget.insert("1.0", results)
    text_widget.pack(expand=True, fill="both")
    root.mainloop()

if __name__ == "__main__":
    show_results()
