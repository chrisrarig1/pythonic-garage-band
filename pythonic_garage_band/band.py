class Band:
    names = []
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        if name not in Band.names:
            Band.names.append(name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        solo = []
        for i in self.members:
             solo.append(i.play_solo())
        return solo

    @classmethod
    def to_list(cls):
        return cls.names






class Musician(Band):
    def __init__(self, name):
        self.name = name
        
    

class Guitarist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
       return f'My name is {self.name} and I play guitar'

    def __repr__(self) -> str:
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return 'guitar'
    
    def play_solo(self):
        return 'face melting guitar solo'

class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
       return f'My name is {self.name} and I play bass'

    def __repr__(self) -> str:
        return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'bass'
    
    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        
    def __str__(self) -> str:
       return f'My name is {self.name} and I play drums'

    def __repr__(self) -> str:
        return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'drums'
    
    def play_solo(self):
        return 'rattle boom crash'