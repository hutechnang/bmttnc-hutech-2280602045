from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:  # Sửa điều kiện vòng lặp while (1 == 1) thành while True
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("************************MENU************************")
    print("** 1. Them sinh vien.                               **")
    print("** 2. Cap nhat thong tin sinh vien boi ID.          **")
    print("** 3. Xoa sinh vien boi ID.                         **")
    print("** 4. Tim kiem sinh vien theo ten.                 **")
    print("** 5. Sap xep sinh vien theo diem trung binh.      **")
    print("** 6. Sap xep sinh vien theo ten chuyen nganh.     **")
    print("** 7. Hien thi danh sach sinh vien.                **")
    print("** 0. Thoat                                        **")
    print("****************************************************")

    try:
        key = int(input("Nhap tuy chon: "))
    except ValueError:
        print("Vui long nhap mot so nguyen tu 0 den 7.")
        continue

    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif key == 2:
        print("\n2. Cap nhat thong tin sinh vien boi ID.")
        if qlsv.soluongSinhVien() > 0:
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 3:
        print("\n3. Xoa sinh vien boi ID.")
        if qlsv.soluongSinhVien() > 0:
            print("\nNhap ID: ")
            ID = int(input())
            if qlsv.deleteByID(ID):
                print(f"\nSinh vien co id = {ID}, da bi xoa.")
            else:
                print(f"\nSinh vien co id = {ID}, khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 4:
        print("\n4. Tim kiem sinh vien theo ten.")
        if qlsv.soluongSinhVien() > 0:
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 5:
        print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
        if qlsv.soluongSinhVien() > 0:
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 6:
        # Chức năng sắp xếp theo tên chuyên ngành chưa được triển khai đầy đủ trong code trước
        print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
        if qlsv.soluongSinhVien() > 0:
            qlsv.sortByName() # Tạm thời sắp xếp theo tên, cần implement sortByMajor nếu cần
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 7:
        print("\n7. Hien thi danh sach sinh vien.")
        if qlsv.soluongSinhVien() > 0:
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 0:
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nVui long chon chuc nang trong hop menu.")