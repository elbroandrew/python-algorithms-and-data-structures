from monitor import Monitor
from computer import Computer
from computer_tower import ComputerTower
from keyboard import Keyboard
from mouse import Mouse
from processor import Processor
from storage import Storage
from memory import Memory


mon = Monitor()
kb = Keyboard()
mouse = Mouse()
ct = ComputerTower(
    Storage(),
    Memory(),
    Processor()
)
comp = Computer(
    monitor=mon,
    computer_tower=ct,
    keyboard=kb,
    mouse=mouse
)
