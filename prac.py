
import sys

f = open('test.txt','rb+')
# for ch in iter(lambda: f.read(1), ''):
#     print(ch,end="")
#


ch=f.read(1)
ch=f.read(1)
ch=f.read(1)

f.seek(-2,1)


ch=f.read(1)

ch=str(ch,'utf-8')

# ch=ch[2:-2]

print(ch)

temp="hello"+str(ch)

print(temp)

f.close()

# ch=f.read(-1)
# print (ch)


# def main():
#     print("Dfdxcx")
#     a="ddfdf\\nd\"fd"
#     print(a)

