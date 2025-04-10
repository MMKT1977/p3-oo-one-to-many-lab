class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]

    def __init__(self,name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"{pet_type} is invalid, must be one of {self.PET_TYPES}")
        
        self.name =name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    

class Owner:
    def __init__(self,name):
        self.name= name
    