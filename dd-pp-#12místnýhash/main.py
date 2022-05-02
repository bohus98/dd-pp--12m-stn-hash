from generators import *
import time
import hashlib


all_lengths = [2]


def main():
    seed = 729150385  # náhodne generovaný
    for length in all_lengths:
        print('length:', length)
        start = time.time()
        print("----------------------------")
        print("BBS")
        bbs = BBS(seed, length)
        if bbs.generate_number():
            print(bbs.generated_number)
            # pass
        else:
            print("Error generating number")
        end = time.time()
        print("Elapsed time:")
        print((end - start) * 1000)
        print("----------------------------")
        print("LCG")
        start = time.time()
        lcg = LCG(length, 32, 7, 0, seed)
        lcg.generate_number()
        print(lcg.generated_number)
        end = time.time()
        print("Elapsed time:")
        print((end - start) * 1000)
        print("----------------------------")
        print("MD5 Hash")
        start = time.time()
        lcg = LCG(length, 32, 7, 0, seed)
        lcg.generate_number()
        lcgstring = str(lcg)
        result = hashlib.md5(lcgstring.encode())
        print(result.hexdigest())
        end = time.time()
        print("Elapsed time:")
        print((end - start) * 1000)
        print("----------------------------")



if __name__ == '__main__':
    main()
