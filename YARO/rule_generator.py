import os


rules = []


def createRule(rule: str, name: str):
    template1 = f"""rule s{name} {{ strings: $ident = """
    template2 = """ condition: $ident }
"""
    return template1 + rule + template2


currentAnswer = ["\x59", "\x33", "\x74",
                 "\x5f", "\x41", "\x6e", "\x30", "\x74", "\x68", "\x33",
                 "\x72", "\x5f", "\x52", "\x33", "\x34", "\x64", "\x5f",
                 "\x4f", "\x70", "\x70", "\x30", "\x72", "\x74", "\x75",
                 "\x6e", "\x31", "\x74"]

FULL_LEN = 28
for i in range(0x20, 0x7e+1):
    string1 = hex(i)[1:]
    length = FULL_LEN-1
    rule = createRule(
        "/ctf4b{"+"".join(currentAnswer)+"\\"+string1+"[\\x20-\\x7e]{"+str(length-len(currentAnswer))+"}}/", hex(i))
    rules.append(rule)

rules = "".join(rules)
with open("./rules.txt", "w") as f:
    f.write(rules)
    f.close()

answer = f"ctf4b{{{(''.join(currentAnswer))}}}"
print(answer)


# os.system("nc yaro-2.beginners.seccon.games 5003 -e test")
# os.system("abcd")
