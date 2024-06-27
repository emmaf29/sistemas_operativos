from utilities.queue import Queue

from hardware.irq import IRQ

from operating_system.pcb import *
from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class RRSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Round Robin Scheduling Algorithm. """

    # TODO (5) Complete the class

    def __init__(self, kernel, quantum):
        self.__kernel = kernel
        self.__quantum = quantum

        self.__ready_queue = Queue()
        self.__already_executed = Queue()
        self.__currently_running = None


    @property
    def next_process_id(self):
        if self.__ready_queue.is_empty :
            self.__already_executed.front
        else :
            self.__ready_queue.front

    
    def move_to_waiting(self, pid, pcb):
        self.__currently_running = None


    
    def move_to_ready(self, pid, pcb):
        self.__ready_queue.enqueue(pid)


    
    def move_to_running(self, pid, pcb):
        if self.__currently_running.state == TERMINATED:
            self.__currently_running = pcb
        else:
            self.__already_executed.enqueue(self.__currently_running)
            self.__currently_running = pcb
            IRQ.DISPATCH(self.is_preemptive)


        

        
