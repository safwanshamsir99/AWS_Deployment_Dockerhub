from pydantic import BaseModel

class Input(BaseModel):
    '''
    num1: first number
    num2: second number
    '''
    num1: float
    num2: float
    
class Output(BaseModel):
    '''
    num3: Addition of num1 and num2
    '''
    num3: float