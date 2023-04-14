from Model import Model
from View import View


class Controller(): # in controller.py
    
    def __init__(self): #init model and view
        self.model = Model() 
        self.view = View(self) #parse controller into view, so the controller can access interface values
        
    def main(self):
        self.view.main()
        

if __name__ == '__main__':
    run = Controller()
    run.main()