import pokebase as pkm
from pokemon import Pokemon
from player import Player
from pokedex import Pokedex

if __name__ == "__main__":

    pokedex = Pokedex()
    joueur = Player("Jordan", [])

    for id in range(1, 5):

        pokemon = pkm.pokemon(id)
        pokemonSpecies = pkm.pokemon_species(id)

        type2 = None
        try:
            if pokemon.types[1]:
                type2 = pokemon.types[1].type.name
        except:
            pass

        statsRaw = pokemon.stats
        baseStats = []
        evYield = []
        for stat in statsRaw:
            baseStats.append(stat.base_stat)
            if stat.effort != 0:
                evYield.append(stat.effort)
            else:
                evYield.append(0)

        if pokemonSpecies.evolves_from_species is not None:
            pkmNameEvolve = pokemonSpecies.evolves_from_species.name
            pokedex.addEvolveToPokemon(pkmNameEvolve, pokemon.name)

        pokemonInfo = {"name": pokemon.name,
                       "id": pokemon.id,
                       "type1": pokemon.types[0].type.name,
                       "type2": type2,
                       "abilityList": pokemon.abilities,
                       "height": pokemon.height,
                       "weight": pokemon.weight,
                       "catchRate": pokemonSpecies.capture_rate,
                       "nationalNumber": pokemonSpecies.pokedex_numbers[0].entry_number,
                       "regionalNumber": pokemonSpecies.pokedex_numbers.pop(0),
                       "genderRatio": pokemonSpecies.gender_rate,
                       "eggGroup": pokemonSpecies.egg_groups,
                       "hatchTime": pokemonSpecies.hatch_counter,
                       "levelingRate": pokemonSpecies.growth_rate,
                       "baseExperienceYield": pokemon.base_experience,
                       "evYield": evYield,
                       "heldItemsList": pokemon.held_items,
                       "locationAreaEncounter": pokemon.location_area_encounters,
                       "movePool": pokemon.moves,
                       "stats": baseStats,
                       "canEvolve": False,
                       "evolveTo": ""}

        pokedex.addPokemonToPokedex(pokemonInfo)
    pokedex.displayPokemonInfo("ivysaur")
