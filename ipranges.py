def range_8_16(CIDR,Range):
    if CIDR > 16 or CIDR < 8:
        print("wrong CIDR only 8-16")
        exit()
    if CIDR == 8:
        CIDR = 0
    if CIDR == 9:
        CIDR = 129
    if CIDR == 10:
        CIDR = 193
    if CIDR == 11:
        CIDR = 225
    if CIDR == 12:
        CIDR = 241
    if CIDR == 13:
        CIDR = 249
    if CIDR == 14:
        CIDR = 253
    if CIDR == 15:
        CIDR = 255
    if CIDR == 16:
        CIDR = 256

    counter = 0
    X = set()

    while True:
        for i in range(0,256):
            X.add(f"{i}.{counter}.0.0/{Range}")
        if counter == CIDR:
            break
        counter += 1
    X = sorted(X, key=lambda x: tuple(map(int, x.split(".")[:2])))
    return X
