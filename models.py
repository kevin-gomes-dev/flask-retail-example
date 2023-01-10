# Contained are all models we will be using

# A shipping address for a customer. Each customer will have 1 shipping address tied to them
class ShipAddr:
    def __init__(self, streetAddr: str, country: str, city: str, state: str, zipCode: str) -> None:
        self.streetAddr = streetAddr
        self.country = country
        self.city = city
        self.state = state
        self.zipCode = zipCode
