# from circular_dependency.a import A
import circular_dependency.a as a


class B:
    def print_dayo(self):
        message = a.A().get_a()
        print(message)
