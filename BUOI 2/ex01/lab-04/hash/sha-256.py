import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes
    return sha256_hash.hexdigest()  # Trả về giá trị băm dưới dạng hex

data_to_hash = input("Nhập dữ liệu để băm bằng SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print(f"Giá trị băm SHA-256: {hash_value}")