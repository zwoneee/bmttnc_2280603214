def tinh_tong_so_chan(Lst):
    tong = 0
    for i in Lst:
        if i % 2 == 0:
            tong += i
    return tong

input_list = input("Nhập một danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(",")))
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong danh sách là:", tong_chan)