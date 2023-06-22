"""This module contains the Gates class.

An instance of the Gates class is composed of several attributes referencing lambda fuctions.
Each lambda fuction contains the logic for various logic gates. (NOT, AND, OR, ect.) 
In addition, an instance of subclass NandConstruction is referenced by the Gates class attribute NAND_CONSTRUCTION
The subclass instance functionaly contains the same logic gates (not, and, or, ect.), but logically constructs the gates 
using ony the nand, "NOT AND", attribute from the Gates class."""


class Gates:
    def __init__(self) -> None:
        self.TRUE = 1
        self.FALSE = 0
        self.NOT = lambda x: 1 - x
        self.AND = lambda x, y: x * y
        self.OR = lambda x, y: x + y - x * y
        self.NOR = lambda x, y: self.NOT(self.OR(x, y))
        self.XOR = lambda x, y: x + y - 2 * x * y
        self.XNOR = lambda x, y: self.NOT(self.XOR(x, y))
        self.NAND = lambda x, y: 1 - (x * y)
        self.NAND_CONSTRUCTION = self.NandConstruction(self.NAND)

    class NandConstruction():
        def __init__(self, nand):
            """Takes nand logic gate and builds other logic gates with it"""
            self.TRUE = 1
            self.FALSE = 0
            self.NOT = lambda x: nand(x, x)
            self.AND = lambda x, y: nand(nand(x, y), nand(x, y))
            self.OR = lambda x, y: nand(nand(x, x),nand(y, y))
            self.NOR = lambda x, y: nand(self.OR(x, y), self.OR(x, y)) 
            self.XOR = lambda x, y: nand(nand(x, nand(x, y)),nand(nand(x, y), y))
            self.XNOR = lambda x, y: nand(self.XOR(x, y), self.XOR(x, y))
            self.NAND = lambda x, y: nand(x, y)
