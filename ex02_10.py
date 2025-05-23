def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

# Sử dụng hàm và in kết quả
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
chuoi_dao_nguoc = dao_nguoc_chuoi(input_string)
print("Chuỗi đảo ngược là:", chuoi_dao_nguoc)