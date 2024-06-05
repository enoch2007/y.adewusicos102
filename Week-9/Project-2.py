import tkinter as tk

class DeliveryService:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Delivery Service")
        self.window.geometry("400x300")

        self.location_var = tk.StringVar()
        self.weight_var = tk.IntVar()

       
        tk.Label(self.window, text="DELIVERY LOCATION:").pack()

      
        tk.Radiobutton(self.window, text="PAU", variable=self.location_var, value="PAU").pack()
        tk.Radiobutton(self.window, text="Epe", variable=self.location_var, value="Epe").pack()

        tk.Label(self.window, text="Package Weight (kg):").pack()

        
        tk.Entry(self.window, textvariable=self.weight_var).pack()

        
        tk.Button(self.window, text="Calculate Cost", command=self.calculate_cost).pack()

    def calculate_cost(self):
        location = self.location_var.get()
        weight = self.weight_var.get()

        if location in ["PAU", "Epe"] and weight >= 10:
            cost = 2000
        else:
            cost = 1500
            

     
        tk.Label(self.window, text=f"Cost: {cost}").pack()


if __name__ == "__main__":
    app = DeliveryService()
    app.window.mainloop()
