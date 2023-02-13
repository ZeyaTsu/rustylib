def init():
    rand = Math()

class Math:
    def getVector(coordsA, coordsB):
        if isinstance(coordsA, list) == False or isinstance(coordsB, list) == False:
            print("RustyLib Error - coordsA or coordsB isn't a list. (Maybe you meant 'coordsA = [x, y]' or 'coordsB = [x, y]')")
        else:
            Vxab = coordsB[0] - coordsA[0]
            Vyab = coordsB[1] - coordsA[1]
            VectorAB = [Vxab, Vyab]
            return VectorAB

    def getVectorNorm(vector):
        if isinstance(vector, list) == False:
            print("RustyLib Error - Vector isn't a list. (Maybe you meant 'vector = [x, y]')")
        else:
            distance = Math.sqrt(vector[0]**2 + vector[1]**2)
            return distance
    
    def getPrime(LIST_NAME):
        Rprime = []
        for i in LIST_NAME:
            index = 0
            for j in range(1, i):
                if i%j == 0:
                    index += 1
            if index == 1:
                Rprime.append(i)
        return Rprime

    def getAllPrime(limit:int=100) -> int:
        numbers = []
        for i in range(limit):
            numbers.append(i)
        RallPrime = Math.getPrime(numbers)
        return RallPrime
    
    def sqrt(num) -> float:
        root = num**(1/2)
        return root
    
    def cubeRoot(num) -> float:
        root = num**(1/3)
        return root
    
    def powerRoot(num, power) -> float:
        root = num**(1/power)
        return root
    
    def rad(angle) -> float:
        rad = angle/180 * Math.pi
        return rad

    def angle(rad) -> float:
        angle = rad/Math.pi * 180
        return angle
    
    def round(number, decimalAllowed=0):
        mul = 10 ** decimalAllowed
        return int(number * mul + 0.5) / mul

    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989