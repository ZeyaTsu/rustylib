import time


"""
initialize some basics
"""
"""
Random Module
"""
class Random:
    def init():
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

    def shuffle(self, LIST_NAME):
        rand = Random()
        rand.seed()
        for _ in range(1):
            for items in LIST_NAME:
                POSITION = rand.rint(0, len(LIST_NAME)-1)
                NEW_POSITION = rand.rint(0, len(LIST_NAME)-1)
                print(POSITION, NEW_POSITION)

                SAVED_ITEM = LIST_NAME.pop(POSITION)
                LIST_NAME.insert(NEW_POSITION, SAVED_ITEM)
        return LIST_NAME
    
    def strio(self, limit, fullCap=False) -> str:
        rand = Random()
        rand.seed()
        STR_C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        FINAL_STR_C_RETURN = []
        if fullCap != True:
            for _ in range(limit):
                POSITION = rand.rint(0, len(STR_C)-1)
                FINAL_STR_C_RETURN.append(STR_C[POSITION])
            FINAL_STR_C_RETURN = ''.join(FINAL_STR_C_RETURN)
        return FINAL_STR_C_RETURN