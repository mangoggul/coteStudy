# s = int(input())
#
# day = s // 86400
# residue = s % 86400
# h = residue // 3600
# residue %= 3600
# m = residue // 60
# residue %= 60
#
# print("%d days %02d:%02d:%02d" % (day, h, m, residue))

# dice1 = int(input())
# dice2 = int(input())
#
# sum = dice1 + dice2
# if sum %3 == 0 and sum % 6 ==0 :
#     print("%d is multiple of 3 and 6" % (sum))
# elif sum % 3 == 0 :
#     print("%d is multiple of 3" %(sum))
# elif sum % 6 == 0 :
#     print("%d is multiple of 6" %(sum))
# else :
#     print("%d is not multiple of 3 or 6" % (sum))
#
#
#


n = int(input())
for i in range(n) :
    for j in range(n-i) :
        print('*' , end = "")
    print()