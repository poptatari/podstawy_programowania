# A stadium is divided into sectors, each marked 
# with a letter. There is a certain number of fans 
# in each sector.

class C:
    def __init__(self, sectors: dict[str, int]):
        self.sectors = sectors

    # Change number of fans in sectors
    def m1(self, s: str, n: int):
        self.sectors[s] = n

    # Returns the sum of fans in the sectors listed in the string s
    def m2(self, s: str) -> int:
        total = 0
        for sector in s:
            if sector in self.sectors:
                total += self.sectors[sector]
        return total


# Sample test cases
stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
stadium.m1("G", 130)

print(stadium.m2("GD"))
print(stadium.m2("KEJ"))