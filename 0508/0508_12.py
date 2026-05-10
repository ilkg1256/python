## Lab: OTP 발생 프로그램

import random

Num = "0123456789"
Passwordlen = 4

Otp = " ".join(random.sample(Num, Passwordlen))
print(Otp)