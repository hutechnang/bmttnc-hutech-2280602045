# Nhập số giờ làm mỗi tuần
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
# Nhập thù lao trên mỗi giờ làm tiêu chuẩn
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
# Số giờ làm chuẩn mỗi tuần
gio_tieu_chuan = 44
# Số giờ làm vượt chuẩn mỗi tuần
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
# Thức lĩnh = lương giờ tiêu chuẩn + lương giờ vượt chuẩn * 150%
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
# In số tiền thực lĩnh của nhân viên
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")