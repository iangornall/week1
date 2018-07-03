def init():
    duplicates_list = ['and', 'and', 'this', 'that', 'and', 'that']
    print remove_duplicates(duplicates_list)

def remove_duplicates(duplicates_list):
    uniques_list = []
    for item in duplicates_list:
        if item not in uniques_list:
            uniques_list.append(item)
    return uniques_list

init()