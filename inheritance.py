class Parent():
    def print_last_name(self):
        print('Silva')


class Child (Parent):

    @staticmethod
    def print_first_name():
        print('Nimesh')

    def print_last_name(self):
        print('Ryan')


nimesh = Child()  # inheritance
nimesh.print_first_name()
nimesh.print_last_name()
