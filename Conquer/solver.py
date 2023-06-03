key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379

flag = "ctf4b{hi_b3g1nner!g00d_1uck_4nd_h4ve_fun!!!}"


def ROL(bits, N):
    for _ in range(N):
        bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
    return bits


flag = bytes_to_long(flag)
length = flag.bit_length()

key = getrandbits(length)
cipher = flag ^ key

for i in range(32):
    key = ROL(key, pow(cipher, 3, length))
    cipher ^= key

print("key =", key)
print("cipher =", cipher)


def ROR(bits, N):
    for _ in range(N):
        bits = (bits >> 1) | ((bits & 1) << (length - 1))
    return bits


for i in range(32):
    cipher ^= key
    key = ROR(key, pow(cipher, 3, length))

cipher = flag ^ key
print(key)
print(flag)
