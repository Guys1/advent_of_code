from advent_of_code_2022_q1_1_input_puzzle import input_puzzle

def number_of_people(input_puzzle):
    number_of_people = 0
    for number_of_elves in input_puzzle:
        if number_of_elves == "":
            number_of_people+=1
    number_of_people+=1
    return number_of_people


def list_for_each_elf(input_puzzle):
    list_input_puzzle = []
    temp_list = []
    for item in input_puzzle:
        if item != "":
            temp_list.append(item)
        else:
            if temp_list:
                list_input_puzzle.append(temp_list)
                temp_list = []
    # for the last group
    if temp_list:
        list_input_puzzle.append(temp_list)
    return list_input_puzzle



# def convert_str_to_list(list_for_elf):
#     """
#     this function gets list that contains many lists that have str values
#     and change them to int
#     [["1","2"][][]]
#     [[1,2][][]]
#     """
#     int_list_of_elf = []
#     for each_list in list_for_elf:
#         print(each_list)
#         int_list_of_elf.append(list(map(int, each_list)))
#     return int_list_of_elf


def convert_str_to_list(str_list):
    int_list = []
    for item in str_list:
        int_list.append(int(item))
    return int_list

def convert_all_str_lists(str_list_in_a_list):
    int_list_in_a_list = []
    for str_list in str_list_in_a_list:
        int_list_in_a_list.append(convert_str_to_list(str_list))
    return int_list_in_a_list


def max_cal(list_for_elf):
    list_of_sums = []
    for list in list_for_elf:
        list_of_sums.append(sum(list))
    return max(list_of_sums)



if __name__ == "__main__":
    num_elf =  number_of_people(input_puzzle)
    print(f"number of people is {num_elf}")
    list_for_elf = list_for_each_elf(input_puzzle)

    int_list_in_a_list = convert_all_str_lists(list_for_elf)
    max_elf = max_cal(int_list_in_a_list)
    print(f"max list of sums is: {max_elf}")




        
    