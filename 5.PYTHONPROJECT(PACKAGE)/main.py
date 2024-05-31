#used for package call
from PACKAGE1 import add
from PACKAGE1 import subt
from PACKAGE1 import multi
from PACKAGE1 import div
from PACKAGE1 import pow
from PACKAGE1 import floor
from PACKAGE1 import modu

#import PACKAGE1

#answer =PACKAGE1.addition(3, 4)
#print(f"The answer is {answer}")

answer =add.addition(3, 4)
print(f"The answer is {answer}")

minus = subt.subtraction(5, 2)
print(f"Subtracting 2 from 5 gives: {minus}")

produc = multi.product(23,5)
print(f"Multiplying 23 and 5 gives: {produc}")

quotient=div.division(78,9)
print(f"Dividing 78 by 9 gives: {quotient}")

power = pow.power(6, 3)
print(f"Raising 6 to the power of 3 gives: {power}")

whole=floor.floordiv(7,8)
print(f"Flooring 7.8 gives: {whole}")

remainder=modu.modulo(7.8,3)
print(f"The remainder when 7.8 is divided by 3 is: {remainder}")