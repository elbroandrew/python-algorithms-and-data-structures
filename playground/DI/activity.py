from monitor import Monitor
from computer import Computer
from computer_tower import ComputerTower
from keyboard import Keyboard
from mouse import Mouse
from processor import Processor
from storage import Storage
from memory import Memory


kb =



class Activity:

    def __init__(self):
        self.monitor = Monitor()
        self.keyboard = Keyboard()
        self.mouse = Mouse()
        self.ct = ComputerTower(
            Storage(),
            Memory(),
            Processor()
        )

        self.comp = Computer(
            monitor=self.monitor,
            computer_tower=self.ct,
            keyboard=self.keyboard,
            mouse=self.mouse
        )
