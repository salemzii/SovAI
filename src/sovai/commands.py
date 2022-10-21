
class Command():
    BANKRUPT = "BANKRUPT"
    _INFO = "INFO"
    _PROB = "PROB"
    _FORC = "FORC"

    allowedCommands = {"BANKRUPT": [_INFO, _PROB, _FORC]}

    def __init__(self) -> None:
        pass
