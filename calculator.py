"""
**NOTE: breezypythongui.py must be in the same directory as this file for proper functionality.

This is a solo attempt at creating a salary calculator for Hunter Business school.
"""
# Import statements.
from breezypythongui import EasyFrame
from tkinter.font import Font
# Class header
class Practice(EasyFrame):
    # Constructor method.
    def __init__(self):
        # Call EasyFrame class constructor
        EasyFrame.__init__(self, title = "Solo Practice Exercise", width = 575, height = 415, resizable = False, background = "salmon")
        self.addLabel(text = "Salary Calculator", sticky = "SEWN", row = 0, column = 0, columnspan = 2, background = "salmon", foreground = "black", font = Font(family = "Courier", size = 26))
        self.addLabel(text = "Hourly Wage:", background = "salmon", row = 1, column = 0, font = Font(size = 22))
        self.addLabel(text = "No. of Hours Worked:", background = "salmon", row = 2, column = 0, font = Font(size = 22))
#       self.addLabel(text = "The employee's salary is:", background = "salmon", row = 4, column = 0, font = Font(size = 22), sticky="E")
        self.wage = self.addFloatField(value = 0.0, row = 1 , column = 1, width = 6)
        self.hours = self.addIntegerField(value = 0, row = 2, column = 1, width = 6)
    # Bind hours variable to [ENTER] input on kbd.
        self.hours.bind("<Return>", lambda event: self.compute())
                # didn't work. Will look into why. This feature is a useful addition...
#       self.salary = self.addFloatField(value = 0.0, row = 4, column = 1, width = 6, sticky="W", state = "readonly", precision = 2)
        self.outputLabel = self.addLabel(text = "", row = 4, column = 0, sticky = "SEWN", columnspan = 2, background = "salmon", foreground = "dark slate gray", font = Font(size = 20))
        self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, state = "normal", command = self.compute)
#       self.compute["background"] = "black"
        self.compute["foreground"] = "salmon"
        self.compute["width"] = 8
        self.compute["height"] = 2
    def compute(self):
        startwage = self.wage.getNumber()
        numHours = self.hours.getNumber()
        payout = startwage * numHours
        self.outputLabel["text"] = "The employee's salary is: $%0.2f" % payout
# Global definition of main().
def main():
    # Instantiate an object from the class into mainloop()
    Practice().mainloop()
# Global call to main()
if __name__ == "__main__":
    main()