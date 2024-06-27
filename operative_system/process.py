from utilities.printer import Printer


EXECUTING = "EXECUTING"
READY = "READY"
BLOCKED = "BLOCKED"
CREATED= "CREATED"    
FINISHED = "FINISHED"

class Process:
    def __init__(self, pid, memory_start, memory_end):
        self._pid = pid
        self._state = CREATED
        self._memory_start = memory_start
        self._memory_end = memory_end
        self._pc = memory_start


    @property
    def pid(self):
        return self._pid
    
    @property
    def state(self):
        return self._state
    
    @property
    def memory_start(self):
        self._memory_start

    @property
    def memory_end(self):
        self._memory_end

    
    def executing(self):
        return self.EXECUTING
    
    def blocked(self):
        return self.BLOCKED
    
    def ready(self):
        return self.READY
    
    def created(self):
        return self.CREATED
    
    def finished(self):
        return self.FINISHED
    
    def __repr__(self):
        return Printer.tabulated([
            ["PID", self._pid],
            ["State", self._state],
            ["M.Start", self._memory_start],
            ["M.End", self._memory_end],
            ["PC", self._pc]

        ])


