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
    

    def testInstruction7(self):
        # Start a new transaction
        self.dataBase.begin_transaction()
    

    def testInstruction8(self):
        self.dataBase.begin_transaction()

        # Expect error for new transaction when one is already in progress 
        with self.assertRaises(RuntimeError):
            self.dataBase.begin_transaction()
    

    def testInstruction9(self):
        self.dataBase.begin_transaction()
        self.dataBase.put("A", 1)
        self.dataBase.commit()

        self.dataBase.begin_transaction()
        self.dataBase.put("B", 2)
        self.dataBase.put("A", 3)

        # Test visibility of transactions
        # We expect 1 and None as outputs for get as they are not visible yet

        self.assertEqual(self.dataBase.get("A"), 1)
        self.assertEqual(self.dataBase.get("B"), None)


    def testInstruction10(self):
        # Test transaction ends after commit
        self.dataBase.begin_transaction()
        self.dataBase.put("A", 1)
        self.dataBase.commit()
        # Verify transaction ended by checking that put raises error
        with self.assertRaises(RuntimeError):
            self.dataBase.put("B", 2) 

        # Test transaction ends after rollback
        self.dataBase.begin_transaction()
        self.dataBase.put("C", 3)
        self.dataBase.rollback()
        # Verify transaction ended by checking that put raises error
        with self.assertRaises(RuntimeError):
            self.dataBase.put("D", 4)  


    def testInstruction11(self):
        # Verify key doesn't exist initially
        self.assertEqual(self.dataBase.get("A"), None)
        self.dataBase.begin_transaction()
        self.dataBase.put("A", 1)
        self.dataBase.commit()

        # Verify future get() can see the committed changes
        self.assertEqual(self.dataBase.get("A"), 1)


    def testInstruction12(self):
        self.dataBase.begin_transaction()
        self.dataBase.put("A", 1)
        self.dataBase.commit()

        # Verify A intially is 1
        self.assertEqual(self.dataBase.get("A"), 1)
        self.dataBase.begin_transaction()
        self.dataBase.put("A", 2)
        self.dataBase.rollback()
        
        # Verify that A is still 1
        self.assertEqual(self.dataBase.get("A"), 1)


if __name__ == "__main__":
    unittest.main()



