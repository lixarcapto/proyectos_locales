

from model.Model import Model
from view.View import View
from controller.Controller import Controller

def main():
    print("iniciado...")
    model = Model()
    view = View()
    controller = Controller(model, view)

main()