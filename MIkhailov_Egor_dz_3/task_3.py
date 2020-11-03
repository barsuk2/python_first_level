def my_func(a,b,c,):
    my_list=[a,b,c]
    my_list.remove(min(my_list))
    # return result_for_recording[0]+result_for_recording[-1]
    return sum(my_list)


print(my_func(9,2,5))
