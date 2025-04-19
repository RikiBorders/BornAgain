import secrets

class BotUtils:
    def __init__(self):
        pass
    
    def rollDice(self, faces: int):
        if not isinstance(faces, int) or faces < 1:
            raise ValueError("The number of faces on the dice must be an integer with a value of at least 1.")
        
        return secrets.randbelow(faces) + 1