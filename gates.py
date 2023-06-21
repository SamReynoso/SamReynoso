class Gates:
    def __init__(self) -> None:
        self.TRUE = lambda : 1
        self.FALSE = lambda : 0
        self.NOT = lambda x: 1 - x
        self.AND = lambda x, y: x * y
        self.OR = lambda x, y: x + y - x * y
        self.XOR = lambda x, y: x + y - 2 * x * y
        self.NAND = lambda x, y: 1 - (x * y)
        self.NAND_CONSTRUCTION = self.NandConstruction(self.NAND)

    class NandConstruction():
        def __init__(self, nand):
            self.NOT = lambda x: nand(x, x)
            self.AND = lambda x, y: nand(nand(x, y), nand(x, y))
            self.OR = lambda x, y: nand(nand(x, x),nand(y, y))
            self.NOR = lambda x, y: nand(self.OR(x, y), self.OR(x, y)) 
            self.XOR = lambda x, y: nand(nand(x, nand(x, y)),nand(nand(x, y), y))
            self.XNOR = lambda x, y: nand(self.XOR(x, y), self.XOR(x, y))
