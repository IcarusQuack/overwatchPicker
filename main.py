import heroes

a = heroes.reinhardt
b = heroes.mercy
c = heroes.soldier76
d = heroes.blank
e = heroes.kiriko
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
    maindpsneeded = False
    offdpsneeded = False
    mainsupportneeded = False
    flexsupportneeded = False
    mainhealerneeded = False
    offhealerneeded = False
    if tank == 0:
        print("Tank needed")
    if totalDps == 0:
        offdpsneeded = True
        maindpsneeded = True
        print("DPS needed")
    if totalDps == 1:
        if mainDps == 1:
            offdpsneeded = True
            print("Off DPS or Situational DPS needed")
        else:
            maindpsneeded = True
            print("Main DPS needed")
    if totalDps == 2:
        if mainDps == 2:
            print("Too many Main DPS")
        if mainDps == 0:
            print("Possibly need Main DPS")
    if totalSupport == 0:
        mainsupportneeded = True
        flexsupportneeded = True
        mainhealerneeded = True
        offhealerneeded = True
        print("Support needed")
    if totalSupport == 1:
        if mainSupport == 1:
            flexsupportneeded = True
            print("Flex Support needed")
        else:
            flexsupportneeded = True
            mainsupportneeded = True
            print("Main Support or Flex Support needed")
        if mainHealer == 1:
            offhealerneeded = True
            print("Off Healer needed")
        elif offHealer == 1:
            mainhealerneeded = True
            print("Main Healer needed")
    if totalSupport == 2:
        if mainSupport == 2:
            print("Too many Main Supports")
        if mainHealer == 2:
            print("Possibly too many Main Healers")
        if offHealer == 2:
            print("Possibily too many Off Healers")
    roletheory = [tank, mainDps, flexDps, mainSupport, flexSupport, mainHealer, offHealer, totalDps, totalSupport,
                  maindpsneeded, offdpsneeded, mainsupportneeded, flexsupportneeded, mainhealerneeded, offhealerneeded]
    return roletheory


def stylePreference(roles, styles):
    totalpicks = roles[0] + roles[7] + roles[8]
    dive = styles[0]
    brawl = styles[1]
    poke = styles[2]
    diving = False
    brawling = False
    poking = False
    compscore = totalpicks + 1
    if totalpicks > 2:
        if dive >= compscore:
            diving = True
            print("This is a great team for diving")
        if brawl >= compscore:
            brawling = True
            print("This is a great team for brawling")
        if poke >= compscore:
            poking = True
            print("This is a great team for poking")
        if diving is False and brawling is False and poking is False:
            print("Cannot confidently decide on a playstyle")
    elif roles[8] == 2:
        if dive >= 4:
            diving = True
            print("This is a great team for diving")
        if brawl >= 4:
            brawling = True
            print("This is a great team for brawling")
        if poke >= 4:
            poking = True
            print("This is a great team for poking")
    else:
        print("Not enough picks to decide a style")
    stylecomp = [diving, brawling, poking, totalpicks]
    print("Total picks:", totalpicks)
    return stylecomp


def suggestHeroes(stylecomp, roles):
    needtank = False
    needdps = False
    needsupport = False
    listofheroes = heroes.listofheroes
    if stylecomp[3] == 5:
        print("Full team")
        return
    if roles[0] == 0:
        needtank = True
    if roles[7] < 2:
        needdps = True
    if roles[8] < 2:
        needsupport = True
    if stylecomp[0] is True:
        print("Suggested Dive Heroes:")
        for x in listofheroes:
            if x['role'] == "tank" and needtank is True and x['dive'] == "yes":
                print(x['name'])
            if x['role'] == "dps" and needdps is True:
                if roles[9] is True and x['theory'] == "mainDps" and x['dive'] == "yes":
                    print(x['name'])
                elif roles[10] is True and x['theory'] == "flexDPS" and x['dive'] == "yes":
                    print(x['name'])
                elif roles[9] is True and x['theory'] == "mainDps" and x['dive'] == "situational":
                    print(x['name'], x['dive'])
                elif roles[10] is True and x['theory'] == "flexDPS" and x['dive'] == "situational":
                    print(x['name'], x['dive'])
                elif x['theory'] == "situationalDps" and x['dive'] == "yes":
                    print(x['name'], x['theory'])
            if x['role'] == "support" and needsupport is True:
                if roles[11] is True and x['theory'] == "mainSupport":
                    if roles[13] is True and x['healerType'] == "mainHealer" and x['dive'] == "yes":
                        print(x['name'])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['dive'] == "yes":
                        print(x['name'])
                    elif roles[13] is True and x['healerType'] == "mainHealer" and x['dive'] == "situational":
                        print(x['name', x['dive']])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['dive'] == "situational":
                        print(x['name', x['dive']])
                elif roles[12] is True and x['theory'] == "flexSupport":
                    if roles[13] is True and x['healerType'] == "mainHealer" and x['dive'] == "yes":
                        print(x['name'])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['dive'] == "yes":
                        print(x['name'])
                    elif roles[13] is True and x['healerType'] == "mainHealer" and x['dive'] == "situational":
                        print(x['name', x['dive']])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['dive'] == "situational":
                        print(x['name', x['dive']])
    if stylecomp[1] is True:
        print("Suggested Brawl Heroes:")
        for x in listofheroes:
            if x['role'] == "tank" and needtank is True and x['brawl'] == "yes":
                print(x['name'])
            if x['role'] == "dps" and needdps is True:
                if roles[9] is True and x['theory'] == "mainDps" and x['brawl'] == "yes":
                    print(x['name'])
                elif roles[10] is True and x['theory'] == "flexDPS" and x['brawl'] == "yes":
                    print(x['name'])
                elif roles[9] is True and x['theory'] == "mainDps" and x['brawl'] == "situational":
                    print(x['name'], x['brawl'])
                elif roles[10] is True and x['theory'] == "flexDPS" and x['brawl'] == "situational":
                    print(x['name'], x['brawl'])
                elif x['theory'] == "situationalDps" and x['brawl'] == "yes":
                    print(x['name'], x['theory'])
            if x['role'] == "support" and needsupport is True:
                if roles[11] is True and x['theory'] == "mainSupport":
                    if roles[13] is True and x['healerType'] == "mainHealer" and x['brawl'] == "yes":
                        print(x['name'])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['brawl'] == "yes":
                        print(x['name'])
                    elif roles[13] is True and x['healerType'] == "mainHealer" and x['brawl'] == "situational":
                        print(x['name', x['brawl']])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['brawl'] == "situational":
                        print(x['name', x['brawl']])
                elif roles[12] is True and x['theory'] == "flexSupport":
                    if roles[13] is True and x['healerType'] == "mainHealer" and x['brawl'] == "yes":
                        print(x['name'])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['brawl'] == "yes":
                        print(x['name'])
                    elif roles[13] is True and x['healerType'] == "mainHealer" and x['brawl'] == "situational":
                        print(x['name', x['brawl']])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['brawl'] == "situational":
                        print(x['name', x['brawl']])
    if stylecomp[2] is True:
        print("Suggested Poke Heroes")
        for x in listofheroes:
            if x['role'] == "tank" and needtank is True and x['poke'] == "yes":
                print(x['name'])
            if x['role'] == "dps" and needdps is True:
                if roles[9] is True and x['theory'] == "mainDps" and x['poke'] == "yes":
                    print(x['name'])
                elif roles[10] is True and x['theory'] == "flexDPS" and x['poke'] == "yes":
                    print(x['name'])
                elif roles[9] is True and x['theory'] == "mainDps" and x['poke'] == "situational":
                    print(x['name'], x['poke'])
                elif roles[10] is True and x['theory'] == "flexDPS" and x['poke'] == "situational":
                    print(x['name'], x['poke'])
                elif x['theory'] == "situationalDps" and x['poke'] == "yes":
                    print(x['name'], x['theory'])
            if x['role'] == "support" and needsupport is True:
                if roles[11] is True and x['theory'] == "mainSupport":
                    if roles[13] is True and x['healerType'] == "mainHealer" and x['poke'] == "yes":
                        print(x['name'])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['poke'] == "yes":
                        print(x['name'])
                    elif roles[13] is True and x['healerType'] == "mainHealer" and x['poke'] == "situational":
                        print(x['name', x['poke']])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['poke'] == "situational":
                        print(x['name', x['poke']])
                elif roles[12] is True and x['theory'] == "flexSupport":
                    if roles[13] is True and x['healerType'] == "mainHealer" and x['poke'] == "yes":
                        print(x['name'])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['poke'] == "yes":
                        print(x['name'])
                    elif roles[13] is True and x['healerType'] == "mainHealer" and x['poke'] == "situational":
                        print(x['name', x['poke']])
                    elif roles[14] is True and x['healerType'] == "offHealer" and x['poke'] == "situational":
                        print(x['name', x['poke']])


roleTheoryList = roleNeeded()
styleCompList = stylePreference(roleTheoryList, calcStyle())
suggestHeroes(styleCompList, roleTheoryList)
