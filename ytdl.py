# import sys
# args = sys.argv
# argsLen = len(args[2:])

# url = sys.argv[1];
# print(args)
# print(argsLen)

from settings import getSettings

DP, VR, SUB, AUO = getSettings()

print(DP, VR, SUB, AUO)
print(type(DP), type(VR), type(SUB), type(AUO))