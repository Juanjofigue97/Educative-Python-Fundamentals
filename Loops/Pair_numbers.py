def check_sum(num_list):
    sum = 0
    cont = 1
    for i in num_list:
      for z in range(cont,len(num_list)):
        check = i + num_list[z]
        if check == 0:
          return True
          break
      cont += 1
    if check != 0:
      return False

print("-------A sum of Zero--------")
print("function which takes in a list and returns \nTrue if the sum of two numbers in the list is zero.")

count = input("how many numbers does the list have?: ")
list_num = []
print("Put the numbers of the list ")
for i in range(int(count)):
    number = int(input())
    list_num.append(number)

print(f"Your list is: {list_num}")

print(check_sum(list_num))

