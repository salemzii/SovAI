from commands import Command 
from exceptions import Exceptions
class Bankrupt():
    FORC = False
    PROB = False
    INFO = False

    def __init__(self, *args) -> None:
        for arg in args:
            if arg == Command._FORC:
                self.FORC = True
            elif arg == Command._INFO:
                self.INFO  = True
            elif arg == Command._PROB:
                self.PROB = True
            else:
                raise(Exceptions.ErrSubCommandNotFound)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
    
    def bankrupt_info(self, *args, **kwargs):
        if self.INFO:
            pass


    def bankrupt_prob(self, *args, **kwargs):
        if self.PROB:
            pass

    def bankrupt_forc(self, *args, **kwargs):
        if self.FORC:
            pass