def func(message):
    print('Got a message: {}'.format(message))

sendMessage = func
sendMessage('Hello world')

# 函数当成参数
def get_message(msg):
    return 'Got a message: ' + msg

def root_call(func, msg):
    print(func(msg))

root_call(get_message, 'Hello world')

# 函数嵌套
def func_test(msg):
    def get_message(msg):
        print('Got a message:{}'.format(msg))
    return get_message(msg)

func_test('Hello world')

# 闭包
def func_closure():
    def get_message(msg):
        print('Got a message:{}'.format(msg))
    return get_message

send_message = func_closure()
send_message('Hello world')