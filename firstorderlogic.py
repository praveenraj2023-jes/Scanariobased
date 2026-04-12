class firstorderknowledgebase:
    def __init__(self):
        self.facts = set()
        self.rules = []
    def addfact(self, propertyname, subject):
        self.facts.add((propertyname, subject))
        print(f"Fact: {subject} is {propertyname}")
    def adduniversalrule(self, ifcondition, thenconclusion):
        self.rules.append((ifcondition, thenconclusion))
        print(f"Rule: {ifcondition} -> {thenconclusion}")
    def forwardchain(self):

        foundnewclues = True
        while foundnewclues:
            foundnewclues = False
            for ifcondition, thenconclusion in self.rules:
                for knownproperty, subject in self.facts.copy():
                    if knownproperty == ifcondition:
                        newfact = (thenconclusion, subject)
                        if newfact not in self.facts:
                            self.facts.add(newfact)
                            print(f"Deduced: {subject} is {thenconclusion}")
                            foundnewclues = True
    def ask(self, propertyname, subject):
        if (propertyname, subject) in self.facts:
            print(f"True: {subject} is {propertyname}")
            return True
        else:
            print(f"Unknown: {subject} is {propertyname}")
            return False
if __name__ == "__main__":
    detective = firstorderknowledgebase()
    detective.adduniversalrule("Reptile", "Cold Blooded")
    detective.adduniversalrule("Snake", "Reptile")
    detective.addfact("Snake", "KaaThePython")
    detective.addfact("Bird", "Tweety")
    detective.forwardchain()
    detective.ask("Cold Blooded", "KaaThePython")
    detective.ask("Cold Blooded", "Tweety")
