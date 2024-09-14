class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Holds pets belonging to this owner

    def pets(self):
        """Return a list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner's list of pets and set the owner for the pet."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of the Pet class can be added.")
        
        pet.owner = self  # Assign the owner to the pet
        self._pets.append(pet)  # Add the pet to the owner's list

    def get_sorted_pets(self):
        """Return a list of pets sorted by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Stores all instances of the Pet class

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type

        # Validate that pet_type is in PET_TYPES
        if pet_type not in self.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        
        self.owner = None  # Initially, the pet may not have an owner

        # If an owner is passed, validate and assign it
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            self.owner = owner
            owner.add_pet(self)  # Add the pet to the owner's list of pets

        # Add this pet instance to the all list
        Pet.all.append(self)
