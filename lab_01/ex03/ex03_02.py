def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập một danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(",")))
dao_nguoc = dao_nguoc_list(numbers)
print("Danh sách đảo ngược là:", dao_nguoc)