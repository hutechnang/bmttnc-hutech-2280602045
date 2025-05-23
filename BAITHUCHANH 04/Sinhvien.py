class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""

from QuanLySinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.soluongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soluongSinhVien(self):
        return len(self.listSinhVien)  # Sử dụng len() thay vì __len__()

    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhập ten sinh vien: ")
        sex = input("Nhập gioi tinh sinh vien: ")
        major = input("Nhập chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhập diem cua sinh vien: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)  # Loại bỏ type hint dư thừa
        if sv:  # Kiểm tra xem sv có tồn tại hay không
            name = input("Nhập ten sinh vien: ")
            sex = input("Nhập gioi tinh sinh vien: ")
            major = input("Nhập chuyen nganh cua sinh vien: ")  # Sửa int thành input cho chuỗi
            diemTB = float(input("Nhập diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien co ID {ID} khong ton tai.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)  # reverse=False là mặc định

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)  # reverse=False là mặc định

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)  # reverse=False là mặc định

    def findByID(self, ID):
        searchResult = None
        if self.soluongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv._id == ID:
                    searchResult = sv
                    return searchResult
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if self.soluongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if listSV:  # Kiểm tra list có rỗng không
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien