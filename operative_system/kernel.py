from operative_system.process  import Process
from hardware.hardware import HARDWARE
from operative_system.long_term_scheduler import LongTermScheduler
from utilities.printer import Printer


class Kernel:
    def __init__(self):
        self._process_table = {}
        self._long_term_scheduler = LongTermScheduler(self, self._process_table)
        self._last_allocated_position = 0 

    def create_process(self, program):
        self._long_term_scheduler.create_process(program)

    def kill_process(self, pid):
        elemenToEliminate = self._process_table.get(pid)
        

    def has_free_memory(self, size):
        return HARDWARE.memory.size - self._last_allocated_position >= size
    
    def allocate(self, data):
        memory_location = self._last_allocated_position
        for i in range(0, len(data)):
            HARDWARE.memory.write(memory_location + i, data[i])
        self._last_allocated_position += len(data)
        return memory_location
    
    def __repr__(self):
        os_config = Printer.tabulated([["No configuration yet"]],
                                    headers=["Configuration"])

        processes = [[], []]
        next_loc = 0
        for _, pcb in self._process_table.intems():
            processes[next_loc].append(pcb)
            next_loc = next_loc % 2

        os_proctable = Printer.tabulated(processes,
                                        headers=["Process Table"])
        return os_config + "\n\n" + os_proctable


            