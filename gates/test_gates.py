import unittest
from gates import Gates


class TestGates(unittest.TestCase):
    gates = Gates()
    nc =gates.NAND_CONSTRUCTION

    data = (0,0), (0,1) ,(1,0), (1,1)    
    class OutPut:    
        AND = 0, 0, 0, 1
        OR = 0, 1, 1, 1
        NOR = 1, 0, 0, 0
        XOR = 0, 1, 1, 0
        XNOR = 1, 0, 0, 1
        NAND = 1, 1, 1, 0
    output = OutPut()

    # Test Givin True
    # Test Givin FALSE
    def test_boolean(self):
        TRUE = 1
        FALSE = 0
        self.assertEqual(self.gates.TRUE, TRUE)
        self.assertEqual(self.gates.FALSE, FALSE)
        self.assertEqual(self.nc.TRUE, TRUE)
        self.assertEqual(self.nc.FALSE, FALSE)

    # Test Negation
    def test_not(self):
        TRUE = 1
        FALSE = 0
        self.assertEqual(self.gates.NOT(TRUE), FALSE)
        self.assertEqual(self.gates.NOT(FALSE), TRUE)
        self.assertEqual(self.nc.NOT(TRUE), FALSE)
        self.assertEqual(self.nc.NOT(FALSE), TRUE)

    def mapper(self, func, output):
        """Test all 4 input pairs"""
        data = self.data
        self.assertEqual(func(data[0][0], data[0][1]), output[0])
        self.assertEqual(func(data[1][0], data[1][1]), output[1])
        self.assertEqual(func(data[2][0], data[2][1]), output[2])
        self.assertEqual(func(data[3][0], data[3][1]), output[3])    

    # Test AND
    def test_and(self):
        self.mapper(self.gates.AND, self.output.AND)    
        self.mapper(self.nc.AND, self.output.AND)
    
    # Test OR
    def test_or(self):
        self.mapper(self.gates.OR, self.output.OR)
        self.mapper(self.nc.OR, self.output.OR)
    
    # Test NOR
    def test_nor(self):
        self.mapper(self.gates.NOR, self.output.NOR)
        self.mapper(self.gates.NOR, self.output.NOR)    

    # Test XOR
    def test_xor(self):
        self.mapper(self.gates.XOR, self.output.XOR)
        self.mapper(self.nc.XOR, self.output.XOR)

    # Test XNOR
    def test_xnor(self):
        self.mapper(self.gates.XNOR, self.output.XNOR)
        self.mapper(self.nc.XNOR, self.output.XNOR)

    # Test NAND
    def test_nand(self):
        self.mapper(self.gates.NAND, self.output.NAND)
        self.mapper(self.nc.NAND, self.output.NAND)

if __name__ == "__main__":
    unittest.main()