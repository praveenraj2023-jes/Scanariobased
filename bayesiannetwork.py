def getchance(iseventhappening, probabilityithappens):
    if iseventhappening == True:
        return probabilityithappens
    else:
        return 1.0 - probabilityithappens
def calculatejointprobability(scenario):
    print(f"Scenario: {scenario}")
    probburglary = getchance(scenario['Burglary'], 0.001)
    probearthquake = getchance(scenario['Earthquake'], 0.002)
    alarmtable = {
        (True, True):   0.950,
        (True, False):  0.940,
        (False, True):  0.290,
        (False, False): 0.001
    }
    currentcondition = (scenario['Burglary'], scenario['Earthquake'])
    probalarm = getchance(scenario['Alarm'], alarmtable[currentcondition])
    johntable = {
        True: 0.90,
        False: 0.05
    }
    probjohncalls = getchance(scenario['JohnCalls'], johntable[scenario['Alarm']])
    marytable = {
        True: 0.70,
        False: 0.01
    }
    probmarycalls = getchance(scenario['MaryCalls'], marytable[scenario['Alarm']])
    print(f"P(Burglary)={probburglary:.5f}")
    print(f"P(Earthquake)={probearthquake:.5f}")
    print(f"P(Alarm|B,E)={probalarm:.5f}")
    print(f"P(John|A)={probjohncalls:.5f}")
    print(f"P(Mary|A)={probmarycalls:.5f}")
    jointprob = probburglary * probearthquake * probalarm * probjohncalls * probmarycalls
    return jointprob
if __name__ == "__main__":
    myscenario = {
        'Burglary': True,
        'Earthquake': False,
        'Alarm': True,
        'JohnCalls': True,
        'MaryCalls': False
    }
    finalprobability = calculatejointprobability(myscenario)
    print(f"Joint Probability: {finalprobability:.10f}")
