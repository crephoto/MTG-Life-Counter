list1 = ["a", "b,", "c"]
list2 = ['1', '2', '3']
list3 = ['xy', 'y', 'z']
list4 = ['7', '8', '9']
alpha_list = [list1, list2, list3, list4]
print(alpha_list[2][0])
player_num = 3
list = [[0]*player_num]*player_num
string = str(list).replace("[", "", 1)
string = string.replace("]", "}", player_num)
string = string.replace("]", "")
string = string.replace("}", "]")
print(string)
#list[len(list)-1, len(list)] = ""