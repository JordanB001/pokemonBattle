
class Pokedex:
    def __init__(self):
        self.pokemonListInfo = []

    def addPokemonToPokedex(self, pokemonInfo):
        self.pokemonListInfo.append(pokemonInfo)

    def addEvolveToPokemon(self, pokemonNameBase, pokemonNameFinal):
        for pokemon in self.pokemonListInfo:
            if pokemon["name"] == pokemonNameBase:
                pokemon["canEvolve"] = True
                pokemon["evolveTo"] = pokemonNameFinal

    def displayPokedexByNationalNumber(self):
        pokemonListInfoOrderByNationalNumber = sorted(self.pokemonListInfo, key=lambda pkm: pkm["nationalNumber"])
        for pokemon in pokemonListInfoOrderByNationalNumber:
            print(str(pokemon["nationalNumber"]) + ": " + pokemon["name"])

    def displayPokedexBy(self, tri):
        pokemonListInfoOrderBy = sorted(self.pokemonListInfo, key=lambda pkm: pkm[tri])
        for pokemon in pokemonListInfoOrderBy:
            print(str(pokemon[tri]) + ": " + pokemon["name"])

    def displayPokemonInfo(self, pokemonName):
        for pokemon in self.pokemonListInfo:
            if pokemon["name"] == pokemonName:
                print(str(pokemon["nationalNumber"]) + ": " + pokemon["name"])
                if pokemon["type2"] is not None:
                    print("types " + pokemon["type1"] + "/" + pokemon["type2"])
                else:
                    print("type " + pokemon["type1"])
                if pokemon["canEvolve"] is True:
                    print("Evolve to " + pokemon["evolveTo"])
                print("height: " + str(pokemon["height"]) + "  weight: " + str(pokemon["weight"]))
                print("-----------------------\n")
                statName = ["PV", "Attaque", "Defense", "Attaque Spe", "Defense Spe", "Vitesse"]
                for i in range(6):
                    print(statName[i] + ": " + str(pokemon["stats"][i]))


