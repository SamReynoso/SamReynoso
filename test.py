import unittest
from gates import Gates


class TestGates(unittest.TestCase):
    gates = Gates()
    data = (0,0), (0,1) ,(1,0), (1,1)    
    
    class OutPut:    
        AND = 0, 0, 0, 1
        NAND = 1, 1, 1, 0
        OR = 0, 1, 1, 1
        NOR = 1, 0, 0, 0
        XOR = 0, 1, 1, 0
        XNOR = 1, 0, 0, 1
    output = OutPut()

    def test_boolean(self):
        self.assertEqual(self.gates.TRUE(), 1)
        self.assertAlmostEqual(self.gates.FALSE(), 0)

    def test_not(self):
        data = 0, 1
        output = 1, 0
        self.assertEqual(self.gates.NOT(data[0]), output[0])
        self.assertEqual(self.gates.NOT(data[1]), output[1])

    def mapper(self, func, output):
        data = self.data
        self.assertEqual(func(data[0][0], data[0][1]), output[0])
        self.assertEqual(func(data[1][0], data[1][1]), output[1])
        self.assertEqual(func(data[2][0], data[2][1]), output[2])
        self.assertEqual(func(data[3][0], data[3][1]), output[3])        

    def test_and(self):
        self.mapper(self.gates.AND, self.output.AND)

    def test_or(self):
        self.mapper(self.gates.OR, self.output.OR)

    def test_xor(self):
        self.mapper(self.gates.XOR, self.output.XOR)
    
    def test_nand(self):
        self.mapper(self.gates.NAND, self.output.NAND)

    def test_nand_not(self):
        NOT = self.gates.NAND_CONSTRUCTION.NOT
        data = 0, 1
        output = 1, 0
        self.assertEqual(NOT(data[0]), output[0])
        self.assertEqual(NOT(data[1]), output[1])
    
    def test_nand_and(self):
        AND = self.gates.NAND_CONSTRUCTION.AND
        self.mapper(AND, self.output.AND)

    def test_nand_or(self):
        OR = self.gates.NAND_CONSTRUCTION.OR
        self.mapper(OR, self.output.OR)

    def test_nand_nor(self):
        NOR = self.gates.NAND_CONSTRUCTION.NOR
        self.mapper(NOR, self.output.NOR)
    
    def test_nand_xor(self):
        XOR = self.gates.NAND_CONSTRUCTION.XOR
        self.mapper(XOR, self.output.XOR)

    def test_nand_xnor(self):
        XNOR = self.gates.NAND_CONSTRUCTION.XNOR
        self.mapper(XNOR, self.output.XNOR)