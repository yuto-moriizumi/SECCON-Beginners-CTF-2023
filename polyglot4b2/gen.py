head = b"".join([b"A" for _ in range(1)])
string = head+b"\n"+b""+b"QUIT\n"
binary = string.decode(encoding="ascii").encode("utf-8")
with open("sample/test.txt", "wb") as f:
    f.write(binary)
    f.close()
