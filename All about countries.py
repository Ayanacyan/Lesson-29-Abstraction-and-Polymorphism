class India():
    def capital(self):
        print("New Dehli is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language in India")
    
    def type(self):
        print("India is a developing nation")

class USA():
    def capital(self):
        print("Washington DC is the capital of the United States")
    
    def language(self):
        print("Most of the population in the USA speaks English")

    def type(self):
        print("USA is a developed country")


obj_ind=India()
obj_usa=USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()