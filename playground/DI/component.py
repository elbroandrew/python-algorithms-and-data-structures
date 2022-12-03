from playground.DI.computer import Computer
from playground.DI.computer_tower import ComputerTower
from playground.DI.keyboard import Keyboard
from playground.DI.memory import Memory
from playground.DI.monitor import Monitor
from playground.DI.mouse import Mouse
from playground.DI.processor import Processor
from playground.DI.storage import Storage


class Component:

    def get_computer(self):
        monitor = Monitor()
        keyboard = Keyboard()
        mouse = Mouse()
        ct = ComputerTower(
            Storage(),
            Memory(),
            Processor()
        )

        return Computer(
            monitor=monitor,
            computer_tower=ct,
            keyboard=keyboard,
            mouse=mouse
        )