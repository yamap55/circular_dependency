# from circular_dependency.b import B
import circular_dependency.b as b


class A:
    def get_a(self):
        return "A DAYO!"


b.B().print_dayo()
