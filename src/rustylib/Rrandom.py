import time


"""
initialize some basics
"""


"""
Random Module
"""
class Random:
    def Rinit():
        rand = Random()
        rand.seed()
        return rand

    def seed(self, seed=None):
        if seed is None:
            seed = int(time.time() * 1000)
        self.seed_value = seed

    def rint(self, IntA, IntB) -> int:
        self.seed_value = (1103515245 * self.seed_value + 12345) & 0xFFFFFFFF
        return IntA + (self.seed_value % (IntB - IntA + 1))
    
    def choice(self, LIST_NAME):
        rand = Random()
        rand.seed()
        POSITION = rand.rint(0, len(LIST_NAME)-1)
        return LIST_NAME[POSITION]
