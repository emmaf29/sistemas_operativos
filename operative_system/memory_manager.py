class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.used_memory = 0

    def has_enough_memory(self, program_length):
        return self.used_memory + program_length <= self.total_memory

    def allocate_memory(self, program_length):
        if not self.has_enough_memory(program_length):
            raise ValueError("No hay suficiente memoria para cargar el programa")
        
        memory_start = self.used_memory
        memory_end = self.used_memory + program_length - 1
        self.used_memory += program_length

        return memory_start, memory_end
    
    