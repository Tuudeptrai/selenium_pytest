class NoSuchElement(Exception):
    """Exception raised for errors in finding of element.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Element not found"):
        self.message = message
        super().__init__(self.message)