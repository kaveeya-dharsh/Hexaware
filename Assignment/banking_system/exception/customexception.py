class InvalidAccountException(Exception):
    def __init__(self, account_number):
        super().__init__(f"Account number {account_number} is invalid or not found.")

class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Withdrawal amount exceeds overdraft limit."):
        super().__init__(message)

class NullPointerException(Exception):
    def __init__(self, message="Unexpected null reference encountered."):
        super().__init__(message)

class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds to perform this operation."):
        super().__init__(message)
