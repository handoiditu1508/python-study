# scope
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    # After local assignment: test spam
    print("After local assignment:", spam)
    do_nonlocal()
    # After nonlocal assignment: nonlocal spam
    print("After nonlocal assignment:", spam)
    do_global()
    # After global assignment: nonlocal spam
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)  # In global scope: global spam
