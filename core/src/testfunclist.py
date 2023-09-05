from ingredidentdetect import r1

my_file = open("flask/output.txt", "r")
data = my_file.read()
data_into_list = data.strip().lower().replace('\n', '').split(",")
data_into_list.remove('')
data_into_list = list(set(data_into_list))


def difference(list1, list2):
    list_dif = [i for i in list1 + list2 if i not in list2]
    return list_dif


r1 = r1

data_into_list = data_into_list

print("Ingredients Needed: " + str(r1))
print("Ingredients Detected: " + str(data_into_list))

# Take difference of list 1 and list 2
z = difference(r1, data_into_list)

# if missing ingredients then say
if not z:
    print("You have all the ingredients, are you ready to start cooking?")
# if all ingredients are present then say
else:
    print("I think you are missing the following ingredients: " + str(z))
