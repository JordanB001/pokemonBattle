class Pokemon:
    def __init__(self, name, ID, nationalNumber, regionalNumber, type1, ability, abilityList, nature, height, weight,
                 gender,
                 genderRatio, catchRate, eggGroup, hatchTime, baseExperienceYield, levelingRate, evYield,
                 heldItemsList, locationAreaEncounter, movePool, movesList, stats, baseStats, type2=None,
                 experience=None, heldItem=None, ev=None, iv=None, canEvolve=False, evolveList=None):
        if ev is None:
            ev = [0, 0, 0, 0, 0, 0]
        if iv is None:
            iv = [0, 0, 0, 0, 0, 0]
        if experience is None:
            experience = 0
        if canEvolve is False:
            evolveList = None

        self.ID = ID
        self.name = name
        self.ability = ability
        self.gender = gender
        self.experience = experience
        self.type1 = type1
        self.type2 = type2
        self.heldItem = heldItem
        self.movePool = movePool
        self.stats = stats
        self.nature = nature
        self.ev = ev
        self.iv = iv

        self.nationalNumber = nationalNumber
        self.regionalNumber = regionalNumber
        self.abilityList = abilityList
        self.baseStats = baseStats
        self.height = height
        self.weight = weight
        self.genderRatio = genderRatio
        self.catchRate = catchRate
        self.eggGroup = eggGroup
        self.hatchTime = hatchTime
        self.baseExperienceYield = baseExperienceYield
        self.levelingRate = levelingRate
        self.evYield = evYield
        self.heldItemList = heldItemsList
        self.locationAreaEncounter = locationAreaEncounter
        self.movesList = movesList

        self.canEvolve = canEvolve
        self.evolveList = []

    def pokemonAddEvolve(self, pokemonName):
        self.evolveList.append(pokemonName)
        self.canEvolve = True
