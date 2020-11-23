from AgentSystem import Agents
from time import sleep
from random import randint
from threading import Thread

class AtmThread(Thread):

    def __init__(self, name, queue, service):
        Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.service = service

    def run(self):
        operations = 20
        id = 0
        while (True):
            if operations == 0:
                break

            operation_time = randint(3, 8)
            args = {
                'id': id,
                'service': self.service,
                'op_time': operation_time
            }
            customer = Agents.Customer(args)
            id += 1

            self.queue.enter(customer)

            if self.service.free:
                self.queue.leave()
                self.service.free = False
                sleep(customer.operation_time)
                self.service.update_count()
                self.service.free = True
                operations -= 1
                print(self.service.operations_count)
                print(self.queue.customers)
            else:
                continue

class ServiceThread(Thread):

    def __init__(self, name, queue, service):
        Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.service = service

    def run(self):
        operations = 20
        id = 0
        while (True):
            if operations == 0:
                break

            operation_time = randint(3, 8)
            args = {
                'id': id,
                'service': self.service,
                'op_time': operation_time
            }
            customer = Agents.Customer(args)
            id += 1

            self.queue.enter(customer)

            if self.service.teller_1.is_free:
                self.queue.leave()
                self.service.teller_1.start_work()
                sleep(customer.operation_time)
                self.service.teller_1.finish_work()
                self.service.update_count()
                operations -=1
                print(self.service.operations_count)
                print(self.queue.customers)

            elif self.service.teller_2.is_free:
                self.queue.leave()
                self.service.teller_2.start_work()
                sleep(customer.operation_time)
                self.service.teller_2.finish_work()
                self.service.update_count()
                operations -=1
                print(self.service.operations_count)
                print(self.queue.customers)

            else:
                continue


if __name__ == '__main__':
    atm_thread = AtmThread('ATM', Agents.AtmQueue(), Agents.ATM())
    service_thread = ServiceThread('Service', Agents.ServiceQueue(), Agents.Service())

    atm_thread.start()
    service_thread.start()

    atm_thread.join()
    service_thread.join()