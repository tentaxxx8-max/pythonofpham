
"""
import math
class hinhtron():
    dem_hinh = 0 
    def __init__(self,bankinh):
        self.bankinh = bankinh
        hinhtron.dem_hinh += 1
    
    def dientich(self):
        return math.pi * (self.bankinh ** 2)
    def chuvi(self):
        return 2 * math.pi * self.bankinh 
    def __str__(self):
        return f"Hinh tron co ban kinh: {self.bankinh}"
    
h1 = hinhtron(5)
h2 = hinhtron(10)
h3 = hinhtron(2.5)

print(h1)
print(f"Dien tich: {h1.dientich()}")
print(f"chu vi: {h1.chuvi()} ")
print("\n" + str(h2))
print(f"Dien tich: { h2.dientich()}")
print("\n" + str(h3))
print(f"Dien tich: {h3.dientich()}")
print(f"tong so hinh tron da tao{hinhtron.dem_hinh}")
"""
"""
Tạo class HinhTron(ban_kinh). Thêm: dien_tich(), chu_vi(), __str__(). Thêm class variable 
dem_hinh đếm số đối tượng đã tạo. Tạo 3 đối tượng HinhTron và in thông tin. 
"""
import math
class hinhtron():
    demhinhtron = 0
    def __init__(self,bankinh):
        self.bankinh = bankinh
        hinhtron.demhinhtron += 1
    def dientich(self):
        # Công thức: S = π * r²
        return math.pi * (self.bankinh ** 2)
    def chuvi(self):
        # Công thức: C = 2 * π * r
        return 2 * math.pi * self.bankinh
    def __str__(self):
        return f"hinh tron nay co ban kinh {self.bankinh}"
h1 = hinhtron(float(input("bankinh1")))
h2 = hinhtron(float(input("bankinh2")))
h3 = hinhtron(float(input("bankinh3")))
print(h1)
print(f"dientich: {h1.dientich()}")
print(f"chu vi: {h1.chuvi()}")
print(str(h2))
print(f"dientich: {h2.dientich()}")
print(f"chu vi: {h2.chuvi()}")
print(str(h3))
print(f"dientich: {h3.dientich()}")
print(f"chu vi: {h3.chuvi()}")
print(f"tong so hinh tron dem duoc{hinhtron.demhinhtron}")