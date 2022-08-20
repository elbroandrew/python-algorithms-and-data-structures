def fun1():
    x1 = 25

    def fun2():
        x1 = 33

        def fun3():
            nonlocal x1
            x1 = 55

        fun3()
        print("fun2.x1 = ", x1) # 55

    fun2()
    print("fun1.x1 = ", x1) # 25

fun1()

# global для глобального, nonlocal для замыкания.