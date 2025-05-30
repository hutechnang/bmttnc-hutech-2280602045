class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        # Bỏ khoảng trắng nếu cần
        text = text.replace(" ", "")
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        num_cols = key
        num_rows = len(text) // key
        if len(text) % key:
            num_rows += 1

        # Tính số ký tự dư (sẽ làm một số cột ngắn hơn)
        num_full_cols = len(text) % key or key

        # Tính số ký tự trên mỗi cột
        col_lengths = [num_rows] * num_cols
        for i in range(num_cols - num_full_cols):
            col_lengths[-(i+1)] -= 1

        # Tách các ký tự vào từng cột
        cols = []
        index = 0
        for cl in col_lengths:
            cols.append(text[index:index + cl])
            index += cl

        # Đọc các ký tự theo hàng
        decrypted_text = ''
        for row in range(num_rows):
            for col in cols:
                if row < len(col):
                    decrypted_text += col[row]
        return decrypted_text
