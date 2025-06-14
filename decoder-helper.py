def extract():
    with open("secret.txt", "r") as f:
        raw = [line.strip() for line in f.readlines()]
    pattern = [3, 7, 0, 6, 2, 5, 4, 1, 8, 9, 10, 11, 12, 13, 14]
    scrambled = [raw[i] for i in pattern]
    for i in range(1, len(scrambled), 2):
        scrambled[i] = scrambled[i][::-1]
    hex_str = ''.join(scrambled)
    data = bytes.fromhex(hex_str)
    key = b'\x68\x74\x74\x70\x73\x3a\x2f\x2f\x64\x72\x69\x76\x65\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x66\x69\x6c\x65\x2f\x64\x2f\x31\x79\x30\x44\x52\x59\x4c\x5a\x37\x2d\x72\x76\x52\x43\x6a\x62\x61\x39\x71\x4a\x68\x4c\x78\x6f\x71\x47\x31\x4a\x4a\x41\x38\x56\x5f\x2f\x76\x69\x65\x77'
    decrypted = bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
    print(decrypted.decode("utf-8"))

if __name__ == "__main__":
    extract()
