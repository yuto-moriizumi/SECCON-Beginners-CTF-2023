# string = b"#include <names.h>"
string = b""


dump = []


# dump.extend([x for x in string])

# dump.extend([0x50, 0x4B, 0x03, 0x04])
# dump.extend([0x00 for i in range(64)])
dump.extend([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])  # png
dump.extend([0x00 for i in range(64)])
# dump.extend([0x89, 0x50, 0x4E, 0x47])
with open("./res", "wb") as f:
    f.write(bytes(dump))
    f.close()
