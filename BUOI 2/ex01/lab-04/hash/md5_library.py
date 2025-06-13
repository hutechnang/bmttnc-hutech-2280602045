import hashlib

def calculate_md5(input_string):
    """
    Tính giá trị băm MD5 của chuỗi đầu vào.
    
    Args:
        input_string (str): Chuỗi cần băm.
    
    Returns:
        str: Giá trị băm MD5 dưới dạng chuỗi hex.
    """
    try:
        md5_hash = hashlib.md5()
        md5_hash.update(input_string.encode('utf-8'))
        return md5_hash.hexdigest()
    except Exception as e:
        return f"Error calculating MD5: {e}"

input_string = input("Nhập chuỗi để băm: ")
md5_hash = calculate_md5(input_string)
print(f"Mã băm MD5 của chuỗi '{input_string}': {md5_hash}")