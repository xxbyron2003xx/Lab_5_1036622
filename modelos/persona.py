import json
class Person:
    def __init__(self, name, dpi, datebirth, address, companies, recluiter, letter = None, conversation = None):
        self.name = name
        self.dpi = dpi
        self.datebirth = datebirth
        self.address = address
        self.companies = companies
        self.recluiter = recluiter
        self.letter = letter if letter is not None else []
        self.conversation = conversation if conversation is not None else []

    def __str__(self):
        return f"Name: {self.name}, DPI: {self.dpi}, Date of Birth: {self.datebirth}, Address: {self.address}, Companies: {self.companies}, Recluiter: {self.recluiter}"

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data["name"], data["dpi"], data["datebirth"], data["address"], data["companies"], data["recluiter"])