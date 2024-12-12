class inMemoryDataBase:
    def __init__(self):
        # Initialize database storage
        self.dataBase = {}
        self.transationDataBase = None
        self.transationInProgress = False
    
    def begin_transaction(self):
        # Starts a new transaction 
        if self.transationInProgress:
            raise RuntimeError("A Transaction is already in progress")
        
        # Initalize a transaction, set up transaction history 
        self.transationDataBase = dict(self.dataBase)
        self.transationInProgress = True
    
    def put(self, key: str, val: int):
        # Put key value pair into database

        # Error Check
        if not self.transationInProgress:
            raise RuntimeError("A Transaction is not in progress")
        if type(key) != str:
            raise RuntimeError("Key is not a string")
        if type(val) != int:
            raise RuntimeError("Value is not an integer")
        
        self.transationDataBase[key] = val
    
    def get(self, key: str) -> int:
        # Get the value associated with the key
        # Only read from main database
        return self.dataBase.get(key, None)
    
    def commit(self):
        # Commit the current transaction
        if not self.transationInProgress:
            raise RuntimeError("A Transaction is not in progress")
        
        self.dataBase = dict(self.transationDataBase)

        # Reset transaction to a unused state
        self.transationDataBase = None
        self.transationInProgress = False
    
    def rollback(self):
        # Rollback the current transaction
        if not self.transationInProgress:
            raise RuntimeError("A Transaction is not in progress")
        
        self.transationDataBase = None
        self.transationInProgress = False




