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
        self.transationDataBase[key] = val
    
    def get(self, key: str) -> int:
        # Get the value associated with the key
        
        # If transaction is in progress, read from trasaction database
        # Otherwise, read from main database
        if self.transaction_in_progress:
            return self.transationDataBase.get(key, None)
        else:
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




