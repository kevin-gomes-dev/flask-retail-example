# Contained are all models we will be using

# A shipping address for a customer. Each customer will have 1 shipping address tied to them
# At the moment, only US addresses are supported
class ShipAddr:
    def __init__(self, streetAddr: str, city: str, state: str, zipCode: str) -> None:
        self.streetAddr = streetAddr
        self.city = city
        self.state = state
        self.zipCode = zipCode
