x= 10
name = "Nang"
is_valid = True
print("Lưu trữ:",x,name,is_valid)
#Cộng (+): Toán tử cộng được dùng để thực hiện phép cộng giữa hai số. 
a = 5
b = 3 
result = a + b
print("Ket Qua Cong:",result)

#Trừ (-): Toán tử trừ được dùng để thực hiện phép trừ giữa hai số. 
a = 8
b = 4 
result = a - b
print("Ket Qua Tru:",result)
#Nhân (*): Toán tử nhân được dùng để thực hiện phép nhân giữa hai số. 
a = 6
b = 7
result = a * b
print("Ket Qua Nhan:",result)
#Chia (/): Toán tử chia được dùng để thực hiện phép chia.
a = 20
b = 5
result = a/b
print("Ket Qua Chia:",result)
#Chia  lấy  phần  nguyên  (//):  Toán  tử  chia  lấy  phần  nguyên  trả  về  kết  quả  là phần nguyên của phép chia.
a = 20
b = 3 
result = a//b
print("Ket Qua Chia  lấy  phần  nguyên:",result)
#Chia lấy dư (%): Toán tử này sẽ cung cấp phần còn lại sau khi thực hiện phép chia giữa hai số.
a = 20
b = 7
remainder = a % b
print("Ket Qua Chia  lấy dư:",result)
#Luỹ thừa (**): Toán tử luỹ thừa được sử dụng để tính toán lũy thừa của một số.
a = 2 
b = 3
result = a ** b
print("Ket Qua Luỹ thừa:",result)
#Các toán tử logic 
#Phép toán AND: Toán tử “and” trả về “True” nếu cả hai điều kiện đều đúng.
x = 5
y = 3
result = (x > 2) and (y < 4) #kết quả: True
print("Ket Qua Phép toán AND:",result)
#Phép toán OR: Toán tử “or” trả về “True” nếu ít nhất một trong hai điều kiện đầu vào là đúng.
x = 5
y = 3
result = (x > 2) or (y < 4) #kết quả: False
print("Ket Qua Phép toán OR:",result)
#Phép toán NOT: Toán tử “not” trả về “True” nếu điều kiện là “False” và ngược lại
x = 5
result = not (x == 5) #kết quả: False
print("Ket Qua Phép toán NOT:",result)
#Phép so sánh bằng (==): Toán tử “==” sẽ so sánh hai giá trị có bằng nhau hay không
x = 5
result = (x == 5) #kết quả: True
print("Ket Qua Phép so sánh:",result)
#Phép  so  sánh không  bằng  (!=):  Toán  tử  “!=” sẽ  so  sánh hai  giá trị  có  khác nhau hay không. 
x = 5
result = (x != 3) #kết quả: True
print("Ket Qua Phép  so  sánh không  bằng:",result)
#Phép so sánh lớn hơn (>), nhỏ hơn (<):
x = 5 
result = (x > 3) #kết quả:True
result = (x < 3) #kết quả: False
print("Kết quả Phép so sánh lớn hơn hoặc nhỏ hơn:",result)
#Phép so sánh lớn hơn hoặc bằng (>=), nhỏ hơn hoặc bằng (<=):
x = 5 
result = (x >= 3) #kết quả:True
result = (x <= 3) #kết quả: False
print("Kết quả Phép so sánh lớn/nhỏ hơn hoặc bằng:",result)

#Nhập, xuất dữ liệu

name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

age = 25
print("Tuổi của bạn là:", age)

print("Python", "là", "ngôn", "ngữ", "lập", "trình", sep="-")
# Kết quả: Python-là- ngôn-ngữ-lập- trình 
print("Xin chào", end="")
print(" các bạn!")# Kết quả: Xin chào các bạn!

#Các cấu trúc điều khiển
#Câu lệnh điều kiện (Conditional Statements):
x = 10
if x > 5:
    print("x lớn hơn 5")
elif x == 5:
    print("x bằng 5")
else:
    print("x nhỏ hơn 5")

#Vòng lặp (Loops)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


count = 0
while count < 5:
    print(count)
    count += 1  # Phải thụt vào bên trong vòng lặp


#Câu lệnh nhảy (Jump Statements)

#Câu lệnh nhảy (Jump Statements)

#Tìm số chia hết cho 5 đầu tiên trong khoảng từ 1 đến 100
for i in range(1, 101) :
    if i % 5 == 0:
     print("Số chia hết cho 5 đầu tiên là:" , i)
    break

# In các số chẵn từ 1 đến 10 và bỏ qua các số lẻ
for i in range(1, 11):
    if i % 2 != 0:
        continue
print(i)

pass
# Kiểm tra điều kiện, nếu đúng thực hiện, nếu sai thì không làm gì
x = 5
if x > 10:
    print("x lớn hơn 10" )
else:
    pass

# Chuỗi
# Khai báo chuỗi trong Python
# Sử dụng dấu ngoặc đơn
string_single_quotes = 'Đây là một chuỗi sử dụng dấu ngoặc đơn.'
# Sử dụng dấu ngoặc kép
string_double_quotes = "Đây là một chuỗi sử dụng dấu ngoặc kép."
# Sử dụng dấu ngoặc ba
string_triple_quotes = '''Đây là một chuỗi sử dụng dâu ngoặc ba, có thể trải dài qua nhiêu dòng '''

# Truy cập ký tự trong chuỗi
my_string = "Hello, World!"
print(my_string[0]) # Kết quả: 'H'
print(my_string[7]) # Kết quả: 'W'

# Các phép xử lý chuỗi trong Python
my_string = "Hello, World!"
print(my_string[7:]) # Lấy từ ký tự thứ 7 đến hết: Kết quả: "World!" 
print(my_string[:5]) # Lấy từ đầu đến ký tự thứ 4: Kết quá: 'Hello' 
print(my_string[3:8])# Lãy từ ký tự thứ 3 đến ký tự thứ 7: Kết quá:
'lo, W'

string1 = "Hello"
string2 = "World"
concatenated_string = string1 +"" + string2 # Kết quả: 'Hello World'

my_string = "Hello, World!"
length = len(my_string) # Kết quả: 13

my_string =" Hello, World!"
print(my_string.strip()) # Loại bỏ khoảng trắng: Kết quả: 'Hello,World!'

my_string = "Hello, World!"
print(my_string.split(","))
# Phân tách chuỗi kết quả: ['Hello', ' World! ']

my_string = "Hello, World!"
print(my_string.replace( "Hello", "Hi"))
# Thay thể chuôi: Kết quả: 'Hi, World!'

# Hàm (Function) 
# Khai báo hàm
def my_function(parameter1, parameter2):
    # Khối mã của hàm
    # Thực hiện các hoạt động dựa trên tham số được truyền vào
    result = parameter1 + parameter2
    return result


# Phân loại hàm:
result = my_function(10, 20) #Gọi hàm và lưu kết quả vào biến  result
print(result) #In kết quả của hàm

# Ví dụ về khai báo và gọi hàm trong Python
# Định nghĩa hàm tính tổng 
def calculate_sum(a, b):
   result= a + b 
   return result
#Gọi hàm và lưu két quá vào biến
sum_result = calculate_sum(10, 20)
#In két qua 
print("Tổng hai số là:", sum_result)

# Ví dụ khai báo và gọi hàm không có giá trị trả về:
#Hàm không trả về giá trị, chỉ in ra thông báo 
def greet (name) :
    print("Xin chào,", name)
# Gọi hàm
greet( "Alice")

from array import array

# Khai báo một mảng số nguyên 
int_array = array('i', [1, 2, 3, 4, 5])

# Khai báo một mảng số thực
float_array = array('f', [3.14, 2.5, 6.7])

# Truy cập phần tử đầu tiên và thứ ba
print(int_array[0])       # Kết quả: 1
print(float_array[2])     # Kết quả: 6.7 (gần đúng)

# Cập nhật phần tử thứ 3 (index 2)
int_array[2] = 10

# Thêm phần tử vào mảng số nguyên
int_array.append(6)

# Xóa giá trị gần đúng với 6.7 trong float_array
for val in float_array:
    if round(val, 2) == 6.7:
        float_array.remove(val)
        break
# In kết quả sau khi cập nhật
print("Mảng số nguyên:", int_array.tolist())
print("Mảng số thực:", float_array.tolist())

# Danh sách (List)
# Khai báo một danh sách (List)

# Danh sách số nguyên
my_list = [1, 2, 3, 4, 5]
# Danh sách chuỗi
names = ["Alice", "Bob", "Charlie"]
# Danh sách kết hợp kiểu dữ liệu
mixed_list = [10, "hello", 3.14, True]

# - Cách sử dụng danh sách:
print(my_list[0])  # Truy cập phần tử đầu tiên: Kết quả: 1
print(names[2])    # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

my_list[1] = 20  # Thay đổi giá trị của phần tử thứ hai
print(my_list)   # Kết quả: [1, 20, 3, 4, 5]

names.append("David")  # Thêm phần tử vào cuối danh sách
print(names)           # Kết quả: ['Alice', 'Bob', 'Charlie', 'David']

del my_list[2]         # Xóa phần tử thứ ba khỏi danh sách
print(my_list)         # Kết quả: [1, 20, 4, 5]

for element in names:
    print(element)     # In từng phần tử trong danh sách

# Kiểu Tuple

# Tuple các số nguyên
my_tuple = (1, 2, 3, 4, 5)
# Tuple các chuỗi
names = ("Alice", "Bob", "Charlie")
# Tuple kết hợp kiểu dữ liệu
mixed_tuple = (10, "hello", 3.14)

# - Truy cập vào phần tử trong Tuple:
print(my_tuple[0])   # Truy cập phần tử đầu tiên: Kết quả: 1
print(names[2])      # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

# - Các phương thức trong Tuple:
my_tuple = (1, 2, 3, 1, 4, 1)
print(my_tuple.count(1))  # Kết quả: 3 (1 xuất hiện 3 lần trong tuple)

my_tuple = ('a', 'b', 'c', 'd', 'b')
print(my_tuple.index('b'))  # Kết quả: 1 (chỉ số đầu tiên của 'b' là 1)

# Kiểu Dictionary

# Khai báo một dictionary rỗng
my_dict = {}

# Khai báo một dictionary với các cặp key-value
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# - Truy cập vào giá trị trong dictionary:
print(person["name"])
print(person["age"])

# - Thêm hoặc cập nhật giá trị trong dictionary:
person["email"] = "alice@example.com"   # Thêm key mới
person["age"] = 26                      # Cập nhật giá trị key đã có

# - Xóa một phần tử trong dictionary:
del person["city"]           # Xóa ssmột cặp key-value
age = person.pop("age")      # Xóa và lấy giá trị key

# - Các phương thức dành cho dictionary:
print(person.keys())    # In ra tất cả các keys
print(person.values())  # In ra tất cả các values
print(person.items())   # In ra tất cả các cặp key-value

# Danh sách (List)

# Khai báo một danh sách (List)
# Danh sách số nguyên
my_list = [1, 2, 3, 4, 5]
# Danh sách chuỗi
names = ["Alice", "Bob", "Charlie"]
# Danh sách kết hợp kiểu dữ liệu
mixed_list = [10, "hello", 3.14, True]

# Cách sử dụng danh sách:
print(my_list[0])  # Truy cập phần tử đầu tiên: Kết quả: 1
print(names[2])    # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

my_list[1] = 20     # Thay đổi giá trị của phần tử thứ hai
print(my_list)      # Kết quả: [1, 20, 3, 4, 5]

names.append("David")  # Thêm phần tử vào cuối danh sách
print(names)           # Kết quả: ['Alice', 'Bob', 'Charlie', 'David']

del my_list[2]       # Xóa phần tử thứ ba khỏi danh sách
print(my_list)       # Kết quả: [1, 20, 4, 5]

for element in names:
    print(element)   # In từng phần tử trong danh sách

# ----------------------------

# Kiểu Tuple

# Tuple các số nguyên
my_tuple = (1, 2, 3, 4, 5)
# Tuple các chuỗi
names = ("Alice", "Bob", "Charlie")
# Tuple kết hợp kiểu dữ liệu
mixed_tuple = (10, "hello", 3.14)

# Truy cập vào phần tử trong Tuple:
print(my_tuple[0])   # Truy cập phần tử đầu tiên: Kết quả: 1
print(names[2])      # Truy cập phần tử thứ ba: Kết quả: 'Charlie'

# Các phương thức trong Tuple:
my_tuple = (1, 2, 3, 1, 4, 1)
print(my_tuple.count(1))  # Kết quả: 3 (1 xuất hiện 3 lần trong tuple)

my_tuple = ('a', 'b', 'c', 'd', 'b')
print(my_tuple.index('b'))  # Kết quả: 1 (chỉ số đầu tiên của 'b')

# ----------------------------

# Kiểu Dictionary

# Khai báo một dictionary rỗng
my_dict = {}

# Khai báo một dictionary với các cặp key-value 
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Truy cập vào giá trị trong dictionary:
print(person["name"])
print(person["age"])

# Thêm hoặc cập nhật giá trị trong dictionary:
person["email"] = "alice@example.com"  # Thêm key mới
person["age"] = 26                     # Cập nhật key đã tồn tại

# Xóa một phần tử trong dictionary:
del person["city"]        # Xóa một cặp key-value
age = person.pop("age")   # Xóa và lấy giá trị của key

# Các phương thức dành cho dictionary:
print(person.keys())      # In ra tất cả các keys
print(person.values())    # In ra tất cả các values
print(person.items())     # In ra tất cả các cặp key-value

# Định nghĩa lớp Car và khởi tạo đối tượng
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model}"

# Tạo đối tượng từ lớp Car và truy cập thông tin
my_car = Car("Toyota", "Corolla")
print(my_car.get_info())  # Kết quả: Toyota Corolla


# Lớp với thuộc tính instance và thuộc tính lớp
class ClassName:
    class_attribute = "Class Attribute"  # Thuộc tính lớp

    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # Thuộc tính instance
        self.attribute2 = attribute2  # Thuộc tính instance

# Tạo đối tượng và truy cập các thuộc tính
object_name = ClassName("value1", "value2")
print(object_name.attribute1)        # Truy cập thuộc tính instance
print(object_name.class_attribute)   # Truy cập thuộc tính lớp


# Lớp với phương thức có tham số
class ClassName:
    def method_name(self, parameter1, parameter2):
        # Các thao tác xử lý
        return f"Parameters: {parameter1}, {parameter2}"

# Gọi phương thức từ đối tượng
object_name = ClassName()
print(object_name.method_name("value1", "value2"))


# Kế thừa trong Python
class ParentClass:
    def greet(self):
        return "Hello from Parent"

class ChildClass(ParentClass):
    def greet_child(self):
        return "Hello from Child"

child = ChildClass()
print(child.greet())        # Kết quả: Hello from Parent
print(child.greet_child())  # Kết quả: Hello from Child


# Đa kế thừa trong Python
class ParentClass1:
    def method1(self):
        return "Method from ParentClass1"

class ParentClass2:
    def method2(self):
        return "Method from ParentClass2"

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        return "Child method"

child = ChildClass()
print(child.method1())       # Kết quả: Method from ParentClass1
print(child.method2())       # Kết quả: Method from ParentClass2
print(child.child_method())  # Kết quả: Child method


# Ghi đè phương thức (Overriding)
class Animal:
    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Đa hình tại thời điểm chạy
def animal_sound(animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()
print(animal_sound(dog))  # Kết quả: Woof!
print(animal_sound(cat))  # Kết quả: Meow!


# Ví dụ về lớp trừu tượng
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Sử dụng các đối tượng từ lớp trừu tượng
dog = Dog()
cat = Cat()
print(dog.make_sound())  # Kết quả: Woof!
print(cat.make_sound())  # Kết quả: Meow!


