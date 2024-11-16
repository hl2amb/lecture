class PortugueseVerb:
    def __init__(self, verb):
        self.verb = verb.lower()
        self.stem = verb[:-2]
        self.ending = verb[-2:]

    def conjugate(self):
        if self.ending == "ar":
            return self._conjugate_ar()
        elif self.ending == "er":
            return self._conjugate_er()
        elif self.ending == "ir":
            return self._conjugate_ir()
        else:
            return "This is not a regular verb."

    def _conjugate_ar(self):
        # -ar 동사의 변형
        conjugations = {
            "eu": self.stem + "o",
            "tu": self.stem + "as",
            "ele/ela/você": self.stem + "a",
            "nós": self.stem + "amos",
            "vós": self.stem + "ais",
            "eles/elas/vocês": self.stem + "am"
        }
        return conjugations

    def _conjugate_er(self):
        # -er 동사의 변형
        conjugations = {
            "eu": self.stem + "o",
            "tu": self.stem + "es",
            "ele/ela/você": self.stem + "e",
            "nós": self.stem + "emos",
            "vós": self.stem + "eis",
            "eles/elas/vocês": self.stem + "em"
        }
        return conjugations

    def _conjugate_ir(self):
        # -ir 동사의 변형
        conjugations = {
            "eu": self.stem + "o",
            "tu": self.stem + "es",
            "ele/ela/você": self.stem + "e",
            "nós": self.stem + "imos",
            "vós": self.stem + "is",
            "eles/elas/vocês": self.stem + "em"
        }
        return conjugations

# print( PortugueseVerb("amar").conjugate())

verb = input("Enter a verb : ")
conjugations = PortugueseVerb(verb).conjugate()
# conjugations = verb.conjugate()


for pronoun, conjugation in conjugations.items():
    print(f"{pronoun}: {conjugation}")

