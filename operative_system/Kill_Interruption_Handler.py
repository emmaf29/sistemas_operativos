from utilities.printer import Printer
from operative_system.irq_handlers.abstract_interruption_handler import AbstractInterruptionHandler

class KillInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        Printer.error("Se está manejando la interrupcion KILL")