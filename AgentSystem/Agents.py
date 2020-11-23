from collections import deque


class Customer:

    def __init__(self, args):
        self.id = args['id']
        self.service = args['service']
        self.operation_time = args['op_time']


class ATM:

    def __init__(self):
        self.free = True
        self.operations_count = 0

    def update_count(self):
        self.operations_count += 1

    def lock_atm(self):
        self.free = False

    def unlock_atm(self):
        self.free = True

class Service:

    def __init__(self):
        self.teller_1 = Teller()
        self.teller_2 = Teller()
        self.operations_count = 0

    def update_count(self):
        self.operations_count += 1

class Teller:

    def __init__(self):
        self.is_free = True

    def start_work(self):
        self.is_free = False

    def finish_work(self):
        self.is_free = True

class Queue:

    def __init__(self):
        self.customers = deque()

    def enter(self, customer):
        self.customers.append(customer)

    def leave(self):
        self.customers.popleft()

class AtmQueue(Queue):

    def __init__(self):
        super().__init__()


class ServiceQueue(Queue):

    def __init__(self):
        super().__init__()
