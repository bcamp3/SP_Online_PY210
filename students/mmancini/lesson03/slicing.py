#!/usr/bin/env python3


####################################


def slice1(in_lst):
    print(f"slice1, original list ", in_lst)

    lst_a = in_lst.copy()
    lst_a = lst_a[-1:] + lst_a[1:-1] + lst_a[:1]

    print(f"slice1, returning swap first and last, ==> ", lst_a)
    return lst_a


def slice2(in_lst):
    print(f"slice2, original list ", in_lst)

    lst_a = in_lst.copy()
    lst_a = lst_a[0::2]

    print(f"slice2, returning every other item removed, ==> ", lst_a)

    return lst_a


def slice_test(in_lst):

    # ***MMM slice syntax notes [begix:endix:step]

    result_lst = in_lst.copy()
    print(f"slice_test, original list ", result_lst)

    # endix = len(in_lst) - 1
	
    lsta = in_lst.copy()
    lsta = lsta[-1:]
    print(f"aaa ", lsta)
    lstb = in_lst.copy()
    lstb = lstb[0:-2]
    print(f"bbb ", lstb)
    lstc = in_lst.copy()
    lstc = lstc[:1]
    print(f"ccc ", lstc)

    print("")

    return result_lst

###################################


# main, test funcs

if __name__ == "__main__":
    # run some tests
    data_lst = ["abc", "def", "hij", "klm", "nop", "qrs"]

    # slice_test(data_lst)

    rslt1 = slice1(data_lst)
    rslt2 = slice2(data_lst)


