def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message):
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    original_length = len(message)
    message += b'\x80' 
    while (len(message) * 8) % 512 != 448:
        message += b'\x00' 
    message += original_length.to_bytes(8, byteorder='little')  

    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], byteorder='little') for j in range(0, 64, 4)]

        a0 = a
        b0 = b
        c0 = c
        d0 = d

        for j in range(64):
            if j < 16:
                f = (b0 & c0) | (~b0 & d0)
                g = j
            elif j < 32:
                f = (d0 & b0) | (~d0 & c0)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b0 ^ c0 ^ d0
                g = (3 * j + 5) % 16
            else:
                f = c0 ^ (b0 | ~d0)
                g = (7 * j) % 16

            f = f + a0 + [0, 0xD76AA478, 0xE8C7B756, 0x242070DB, 0xC1BDCEEE, 0xF57C0FAF, 0x4787C62A, 0xA8304613,
                          0xFD469501, 0x698098D8, 0x8B44F7AF, 0xFFFF5BB1, 0x895CD7BE, 0x6B901122, 0xFD987193,
                          0xA679438E, 0x49B40821, 0xF61E2562, 0xC040B340, 0x265E5A51, 0xE9B6C7AA, 0xD62F105D,
                          0x02441453, 0xD8A1E681, 0xE7D3FBC8, 0x21E1CDE6, 0xC33707D6, 0xF4D50D87, 0x455A14ED,
                          0xA9E3E905, 0xFCEFA3F8, 0x676F02D9, 0x8D2A4C8A, 0xFFFA3942, 0x8771F681, 0x6D9D6122,
                          0xFDE5380C, 0xA4BEEA44, 0x4BDECFA9, 0xF6BB4B60, 0xBEBFBC70, 0x289B7EC6, 0xEAA127FA,
                          0xD4EF3085, 0x04881D05, 0xD9D4D039, 0xE6DB99E5, 0x1FA27CF8, 0xC4AC5665, 0xF4292244,
                          0x432AFF97, 0xAB9423A7, 0xFC93A039, 0x655B59C3, 0x8F0CCC92, 0xFFEFF47D, 0x85845DD1,
                          0x6FA87E4F, 0xFE2CE6E0, 0xA3014314, 0x4E0811A1, 0xF7537E82, 0xBD3AF235, 0x2AD7D2BB,
                          0xEB86D391][j] + words[g]
            temp = d0
            d0 = c0
            c0 = b0
            b0 = b0 + left_rotate(f, [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
                                     5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
                                     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
                                     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21][j])
            a0 = temp

        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF

    return f"{a:08x}{b:08x}{c:08x}{d:08x}"

input_string = input("Nhập chuỗi để băm: ")
md5_hash = md5(input_string.encode('utf-8'))
print(f"Mã băm MD5 của chuỗi '{input_string}': {md5_hash}")