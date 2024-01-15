
#Name : ERIC AMOH ADJEI
#Date : 11/11/2023
#Assignment : Final Project: 
#An overview of the MultiApp code, explaining its structure, functionality, and usage.
#Application and Presentation Video


##-----------------------------------##


# Imports: The code imports necessary modules such as 
#- `tkinter`, `ttk`, `ttkbootstrap`,PIL, and others we will need to run the app.
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from turtle import color
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
from PIL import Image, ImageTk
import requests
import random
import time

# Loading Screen: The code begins by setting up a loading screen using the `time` module.
# setting loading time for the application to run smooth.
load_time = 2 # seconds
load_time2= 4#seconds

# loading screen for 3 seconds
print("\t \t \n Loading app...\t \n")
time.sleep(load_time)

print("\t \n   ...\n")
time.sleep(load_time)
print(f"App loaded after {load_time2}seconds")


# Description:  ND USER INTRO , Final Project: Application and Presentation Video
print(" \n \n \t\t\t Welcome to our Final Project: An overview of the MultiApp code, \n \t explaining its structure, functionality, and usage \n \n \t\t")

#An opening description of the application and instructions for the user are displayed on the screen.
print(" \n \n \t In this Final, we will create a Python application.  \n  \t That do something not just be an ad hoc demo of the requirement \n \t\t")

#time slows app loading times
time.sleep(load_time)

# application taking User Input
name = input(" Before we begin, What is your good name? \n :")
print(" \n \n \t\t\t Nice to meet you\n " + name + " .\n\t \t")

time.sleep(load_time)

# application Output to the Display
print("\n \t Should you come by any question? \n \t I mean please, if you have any query, write it down and ask later: \n")
print("\n \t \t From here the application will be show-casing in just 4 seconds ( Should pop up), \n")

time.sleep(load_time2)

# Main Class - MultiApp: The `MultiApp` class is the core of the application.
# and Shared variables for weather, expense tracker, to-do list, and expense history are initialized.
# also Creating a class call multi app to hold my combine applications and functions
class MultiApp:
    
    #Including at least 3 functions.
    def __init__(self, root):
        self.root = root
        self.root.title("Personal MultiApp NoteBook")
        
        #next we will need to set the minimum size of the window
        root.minsize(width=200, height=220)
        
        # application containing variables with at least two different data types.
        #next we will need to create a text label,height,width,font.
        text_result = tk.Text(root, height=2, width=16, font=("Open sans", 24))

        #-----------------------------------------------------------------------#
        """
        # creaing a code to Load the background image 
        bg_image = Image.open("screenshot.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        
        # Create a Canvas widget and place the background image on it
        canvas = tk.Canvas(root, width=bg_image.width, height=bg_image.height)
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

        # Create a label to display the background image
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)  # Covers the entire window
        """""""""
        #-----------------------------------------------------------------------#
        
        # creating a Shared variables and inserting my api key from open weather map
        self.weather_api_key = 'f223c151181072bd0b2292d3f58d2149'
        self.weather_result_str = tk.StringVar()
        self.expense_tracker = {'Category': tk.StringVar(), 'Amount': tk.DoubleVar()}
        self.to_do_list = {'Task': tk.StringVar()}
        self.expense_history = []
        
        # Tabs Setup: Tabs for Weather, Expense Tracker, and To-Do List are created using `ttk.Notebook`.
        # Creating app tabs
        self.notebook = ttk.Notebook(root)
        
        # Weather Tab: The Weather tab allows users to input a city and fetch weather information.
        # Creating app Weather Tab
        self.weather_frame = tk.Frame(self.notebook)
        self.setup_weather_tab()
        
        #Creating app Expense Tracker Tab : The Expense Tracker tab enables users to add, show, and clear expenses.
        self.expense_frame = tk.Frame(self.notebook)
        self.setup_expense_tab()

        #Creating app To-Do List Tab : The To-Do List tab allows users to add, show, and clear tasks.
        self.todo_frame = tk.Frame(self.notebook)
        self.setup_todo_tab()


        #Creating app Pack notebook
        self.notebook.add(self.weather_frame, text="Weather")
        self.notebook.add(self.expense_frame, text="Expense Tracker")
        self.notebook.add(self.todo_frame, text="To-Do List")
        self.notebook.pack(expand=1, fill="both")


    # Creating a function to get weather information from openweathermap.org
    def setup_weather_tab(self):
        tk.Label(self.weather_frame, text="Enter city for weather:").pack()
        city_entry = tk.Entry(self.weather_frame)
        city_entry.pack(padx=3, pady=8)
        tk.Button(
            self.weather_frame,
            text="Get Weather",
            command=lambda: self.get_weather(city_entry.get())
        ).pack(padx=3, pady=5)


    # Creating a function to display weather information
        tk.Label(self.weather_frame, text="Weather Information:").pack()
        result_label = tk.Label(self.weather_frame, textvariable=self.weather_result_str)
        result_label.pack(padx=3, pady=8)
        

    # Creating a function to get weather information from openweathermap.org
    def get_weather(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': self.weather_api_key,
            'units': 'metric'
        }

    # Getting weather information from openweathermap.org
        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            # Checking if the response is successful
            # Including at least 1 control structure (if/else and/or loops).
            if response.status_code == 200:
                weather_info = (
                    f"\nCity: {data['name']}\n"
                    f"Temperature: {data['main']['temp']}°C\n"
                    f"Condition: {data['weather'][0]['description']}\n"
                    f"Humidity: {data['main']['humidity']}%\n"
                    f"Wind Speed: {data['wind']['speed']} m/s"
                )
                self.weather_result_str.set(weather_info)

                # If the response is not successful, print the error message
            else:
                messagebox.showerror("Error", f"Failed to fetch weather: {data['message']}")

            # If the response is not successful, print the error message
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")



    #Creating my expense tracker UI elements and logic here
    def setup_expense_tab(self):
        tk.Label(self.expense_frame, text="Expense Tracker").pack()
        

        #Creating app Expense Tracker UI elements
        category_label = tk.Label(self.expense_frame, text="Category:")
        category_label.pack(padx=2, pady=5)
        category_entry = tk.Entry(self.expense_frame, textvariable=self.expense_tracker['Category'])
        category_entry.pack(padx=2, pady=5)
        amount_label = tk.Label(self.expense_frame, text="Amount:")
        amount_label.pack(padx=2, pady=5)
        amount_entry = tk.Entry(self.expense_frame, textvariable=self.expense_tracker['Amount'])
        amount_entry.pack(padx=2, pady=5)
        add_expense_button = tk.Button(self.expense_frame, text="Add Expense", command=self.add_expense)
        add_expense_button.pack(padx=3, pady=8)


        #Creating app Buttons for showing and clearing expenses
        show_expenses_button = tk.Button(self.expense_frame, text="Show Expenses", command=self.show_expenses)
        show_expenses_button.pack(padx=5, pady=10)
        clear_expenses_button = tk.Button(self.expense_frame, text="Clear Expenses", command=self.clear_expenses)
        clear_expenses_button.pack(padx=5, pady=10)


        #Creating app Expense Tracker UI layout
        category_label.pack()
        category_entry.pack()
        amount_label.pack()
        amount_entry.pack()
        add_expense_button.pack()
        show_expenses_button.pack()
        clear_expenses_button.pack()


    # Creating a function to add expenses to the expense tracker
    def add_expense(self):
        category = self.expense_tracker['Category'].get()
        amount = self.expense_tracker['Amount'].get()

    # Checking if both category and amount are entered
        if category and amount:
            messagebox.showinfo("Expense Added", f"Expense added: Category - {category}, Amount - {amount}")

            # Adding further logic for storing the expense data as needed
        else:
            messagebox.showwarning("Warning", "Please enter both Category and Amount.")


    # Adding the expense to the history
        self.expense_history.append(f"Category: {category}, Amount: {amount}")

    # Creating a function to show the expense history
    def show_expenses(self):
        
        # Showing the expense history
        expenses_str = "\n".join(self.expense_history)
        messagebox.showinfo("Expense History", expenses_str)

# Clearing the expense history
    def clear_expenses(self):

        # Clearing the expense history
        self.expense_history = []
        messagebox.showinfo("Expenses Cleared", "Expense history has been cleared.")



# Creating my to-do list UI elements and logic here, The To-Do List tab allows users to add, show, and clear tasks
# And Using at least one List, Tuple, Set, or Dictionary here.
    def setup_todo_tab(self):
        tk.Label(self.todo_frame, text="To-Do List").pack()


        # Creating app to-do list UI elements and logic here
        # To-Do List UI elements
        task_label = tk.Label(self.todo_frame, text="Task:")
        task_label.pack(padx=2, pady=5)
        task_entry = tk.Entry(self.todo_frame, textvariable=self.to_do_list['Task'])
        task_entry.pack(padx=2, pady=5)
        add_task_button = tk.Button(self.todo_frame, text="Add Task", command=self.add_task)
        add_task_button.pack(padx=3, pady=8)


        # Creating app Buttons for showing and clearing tasks
        show_tasks_button = tk.Button(self.todo_frame, text="Show Tasks", command=self.show_tasks,)
        show_tasks_button.pack(padx=5, pady=10)
        clear_tasks_button = tk.Button(self.todo_frame, text="Clear Tasks", command=self.clear_tasks)
        clear_tasks_button.pack(padx=5, pady=10)


        #Creating app To-Do List UI layout
        task_label.pack()
        task_entry.pack()
        add_task_button.pack()
        show_tasks_button.pack()
        clear_tasks_button.pack()


    # Creating a function to add tasks to the to-do list
    def add_task(self):
        task = self.to_do_list['Task'].get()
        

    # Checking if the task is entered
        if task:
            messagebox.showinfo("Task Added", f"Task added: {task}")

            # Adding further logic for storing the task data as needed
        else:
            messagebox.showwarning("Warning", "Please enter a task.")


    # Adding the task to the task list
    def show_tasks(self):
        # Showing the task list
        tasks_str = "\n".join(self.to_do_list['Task'].get())
        messagebox.showinfo("Task List", tasks_str)


    # Clearing the task list
    def clear_tasks(self):
        # Clears the task list
        self.to_do_list['Task'].set('')
        messagebox.showinfo("Tasks Cleared", "Task list has been cleared.")


# Main Function: The `main()` function initializes the application.
# Creating my calculator UI elements and logic here
#Styles and Themes: The `ttk.Style` class is used to configure the appearance of widgets.
def main():
    root = tk.Tk()
    style = ttk.Style("darkly")
    app = MultiApp(root)
    root.mainloop()
    

# Executing the App: The script checks if it's the main module and runs the app.
# Creating a logic for the app UI here
if __name__ == "__main__":
    main()