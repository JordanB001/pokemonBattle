class Player:
    def __init__(self, name, equipe):
        self.name = name
        self.equipe = equipe

    def addPokemon(self, pokemon):
        self.equipe.append(pokemon)
