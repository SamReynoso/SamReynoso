import unittest
from gates import Gates


class TestGates(unittest.TestCase):
    data = (0,0), (0,1) ,(1,0), (1,1)
    gates = Gates()

    def test_boolean(self):
        self.assertEqual(self.gates.TRUE(), 1)
        self.assertAlmostEqual(self.gates.FALSE(), 0)

    def test_not(self):
        data = 0, 1
        out_put = 1, 0
        self.assertEqual(self.gates.NOT(data[0]), out_put[0])
        self.assertEqual(self.gates.NOT(data[1]), out_put[1])

    def mapper(self, func, output):
        data = self.data
        self.assertEqual(func(data[0][0], data[0][1]), output[0])
        self.assertEqual(func(data[1][0], data[1][1]), output[1])
        self.assertEqual(func(data[2][0], data[2][1]), output[2])
        self.assertEqual(func(data[3][0], data[3][1]), output[3])        

    def test_and(self):
        output = 0, 0, 0, 1
        self.mapper(self.gates.AND, output)

    def test_or(self):
        output = 0, 1, 1, 1
        self.mapper(self.gates.OR, output)

    def test_xor(self):
        output = 0, 1, 1, 0
        self.mapper(self.gates.XOR, output)
    
    def test_nand(self):
        output = 1, 1, 1, 0
        self.mapper(self.gates.NAND, output)


    def test_nand_not(self):
        NOT = self.gates.NAND_CONSTRUCTION.NOT
        data = 0, 1
        output = 1, 0
        self.assertEqual(NOT(data[0]), output[0])
        self.assertEqual(NOT(data[1]), output[1])
    
    def test_nand_and(self):
        AND = self.gates.NAND_CONSTRUCTION.AND
        output = 0, 0, 0, 1
        self.mapper(AND, output)

    def test_nand_or(self):
        OR = self.gates.NAND_CONSTRUCTION.OR
        output = 0, 1, 1, 1
        self.mapper(OR, output)

    def test_nand_nor(self):
        NOR = self.gates.NAND_CONSTRUCTION.NOR
        output = 1, 0, 0, 0
        self.mapper(NOR, output)
    
    def test_nand_xor(self):
        XOR = self.gates.NAND_CONSTRUCTION.XOR
        output = 0, 1, 1, 0
        self.mapper(XOR, output)

    def test_nand_xnor(self):
        XNOR = self.gates.NAND_CONSTRUCTION.XNOR
        output = 1, 0, 0, 1
        self.mapper(XNOR, output)