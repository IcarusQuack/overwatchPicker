import heroes

a = heroes.sigma
b = heroes.cassidy
c = heroes.pharah
d = heroes.ana
e = heroes.baptiste
heroList = [a, b, c, d, e]


def calcStyle():
    dive = 0
    brawl = 0
    poke = 0
    # calculate dive score
    for x in heroList:
        if x['dive'] == "yes":
            if x['role'] == "dps":
                dive += 1
            else:
                dive += 2
        elif x['dive'] == "situational":
            if x['role'] == "dps":
                dive += .5
            else:
                dive += 1
    # calculate brawl score
    for x in heroList:
        if x['brawl'] == "yes":
            if x['role'] == "dps":
                brawl += 1
            else:
                brawl += 2
        elif x['brawl'] == "situational":
            if x['role'] == "dps":
                brawl += .5
            else:
                brawl += 1
    # calculate poke score
    for x in heroList:
        if x['poke'] == "yes":
            if x['role'] == "dps":
                poke += 1
            else:
                poke += 2
        elif x['poke'] == "situational":
            if x['role'] == "dps":
                poke += .5
            else:
                poke += 1
    print("dive score is", dive)
    print("brawl score is", brawl)
    print("poke score is", poke)
    stylescores = [dive, brawl, poke]
    return stylescores


def roleNeeded():
    tank = 0
    mainDps = 0
    flexDps = 0
    mainSupport = 0
    flexSupport = 0
    mainHealer = 0
    offHealer = 0
    totalDps = 0
    totalSupport = 0
    # Adding heroes
    for x in heroList:
        if x['theory'] == "tank":
            tank += 1
        elif x['theory'] == "mainDps":
            mainDps += 1
            totalDps += 1
        elif x['theory'] == "flexDPS":
            flexDps += 1
            totalDps += 1
        elif x['theory'] == "situationalDps":
            totalDps += 1
        elif x['theory'] == "mainSupport":
            totalSupport += 1
            mainSupport += 1
        elif x['theory'] == "flexSupport":
            totalSupport += 1
            flexSupport += 1
        if x['role'] == "support":
            if x['healerType'] == "mainHealer":
                mainHealer += 1
            else:
                offHealer += 1
    # Printing out what role is needed
    if tank == 0:
        print("Tank needed")
    if totalDps == 0:
        print("Need DPS")
    if totalDps == 1:
        if mainDps == 1:
            print("Need Off DPS or Situational DPS")
        else:
            print("Need Main DPS")
    if totalDps == 2:
        if mainDps == 2:
            print("Too many Main DPS")
        if mainDps == 0:
            print("Possibly need Main DPS")
    if totalSupport == 0:
        print("Need Support")
    if totalSupport == 1:
        if mainSupport == 1:
            print("Flex Support needed")
        else:
            print("Main Support or Flex Support needed")
        if mainHealer == 1:
            print("Off Healer needed")
        elif offHealer == 1:
            print("Main Healer needed")
    if totalSupport == 2:
        if mainSupport == 2:
            print("Too many Main Supports")
        if mainHealer == 2:
            print("Possibly too many Main Healers")
        if offHealer ==2:
            print("Possibily too many Off Healers")
    roletheory = [tank, mainDps, flexDps, mainSupport, flexSupport, mainHealer, offHealer, totalDps, totalSupport]
    return roletheory


calcStyle()
roleNeeded()
