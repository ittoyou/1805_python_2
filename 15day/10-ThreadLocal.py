
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)#线程
    do_task_2(std)#线程2

def do_task_1(std):
    do_subtask_1(std)#线程
    do_subtask_2(std)#线程

def do_task_2(std):
    do_subtask_2(std)#
    do_subtask_2(std)



global_dict = {}#声明全局字典

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    ...    


t1 = Thread(target = std_thread)    
t2 = Thread(target = std_thread)




import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=(‘laozhao',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('xiaoyuan',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()




