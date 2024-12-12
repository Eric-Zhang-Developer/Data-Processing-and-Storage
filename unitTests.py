import unittest
from inMemoryDataBase import inMemoryDataBase

class testInMemoryDataBase(unittest.TestCase):
    def setUp(self):
        self.dataBase = inMemoryDataBase()

    def testBasicTransactionWorkflow(self):
        # Test a complete transaction workflow
        self.dataBase.begin_transaction()
        self.dataBase.put("test_key", 123)
        self.dataBase.commit()
        
        # Verify the value was stored correctly
        self.assertEqual(self.dataBase.get("test_key"), 123)
    
    def testInstruction2(self):
        self.dataBase.begin_transaction()

        # Test for invalid key input
        with self.assertRaises(RuntimeError):
            self.dataBase.put(123, 456) 
    
        # Test for invalid value input
        with self.assertRaises(RuntimeError):
            self.dataBase.put("test_key", "bruh")

        # Test normal input
        self.dataBase.put("test_key", 123)  
    
    def testInstruction3(self):
        self.dataBase.begin_transaction()

        # Test creating new key
        self.dataBase.put("A", 5)
        self.dataBase.commit()
        self.assertEqual(self.dataBase.get("A"), 5)

        # Test updating existing key
        self.dataBase.begin_transaction()
        self.dataBase.put("A", 10)  # Update existing key A
        self.dataBase.commit()
        self.assertEqual(self.dataBase.get("A"), 10)  # Value should be updated
    
    def testInstruction4(self):
        self.dataBase.begin_transaction()

        # Test getting value associated with key
        self.dataBase.put("A", 10)
        self.dataBase.commit()
        self.assertEqual(self.dataBase.get("A"), 10)

        # Test getting a non existent key 
        self.assertEqual(self.dataBase.get("B"), None)
    
    def testInstruction5(self):
        # Checks if put not during an transaction will throw an exception
        with self.assertRaises(RuntimeError):
            self.dataBase.put("A", 10)

    def testInstruction6(self):

        # Check for get outside of a transaction
        self.assertEqual(self.dataBase.get("A"), None)

        # Check functionality of get inside a transaction
        self.dataBase.begin_transaction()
        self.assertEqual(self.dataBase.get("A"), None)




        

    




if __name__ == "__main__":
    unittest.main()



