from hardware.hardware import HARDWARE

from operative_system.process import Process

class LongTermScheduler:
    def __init__(self, kernel, process_table):
        self._kernel = kernel
        self._process_table = process_table
        self._next_pid = 1


    def create_process(self, program):
            memory_location = self._allocate_program_in_memory(program)
            self._created_pcb(program, memory_location)
            self._increase_next_pid()
     
    def _allocate_program_in_memory(self, program):
        if self._kernel.has_free_memory(len(program.instructions)):
            return self._kernel.allocate(program.instructions)
        else:
            raise Exception("no hay memoria suficiente")

    def _created_pcb(self, program, memory_location):
        self._process_table[self._next_pid] = Process(
        self._next_pid,
        memory_location,
        memory_location + len(program.instructions))
          
    def _increase_next_pid(self):
        self._next_pid += 1
            
        



    
    




