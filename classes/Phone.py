class Phone:
    __serial_number: str
    __color: str

    def __init__(self, made, model, price, ):
        self.made = made
        self.price = price
        self.model = model

    def desc_phone(self):
        print(f'made: {self.made} model: {self.model} price: {self.price}')

    def callNumber(self, phone_number: str):
        print(f'calling...{phone_number}')

    def set_serial_number(self, __serial_number):
        self.__serial_number = __serial_number

    def get_serial_number(self):
        return self.__serial_number

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color
