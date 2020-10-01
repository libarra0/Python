
# class VotingBooth:

#     def __init__(self, identifier, country):
#         self._identifier = identifier
#         self._country = country
#         self._region = None

#     @property
#     def region(self):
#         return self._region

#     @property.setter
#     def set_region(self, region):
#         if region in self._country:
#             self._region = region
#         else:
#             raise ValueError(f'The region {region} is not in the {self._country}')

# def run():
#     voting_booth = VotingBooth(123, ['Mexico','Morelos'])
#     print(voting_booth.region)
#     voting_booth.region = "Mexico"
#     print(voting_booth.region)

class Geeks: 
    def __init__(self): 
        self._age = 0
        
    # using property decorator
    # a getter function 
    @property
    def age(self):
        print("getter method called")
        return self._age 
       
     # a setter function 
    @age.setter 
    def age(self, a):
        if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a

def run():
    mark = Geeks()
    mark.age = 19
    print(mark.age)


if __name__ == "__main__":
    run()