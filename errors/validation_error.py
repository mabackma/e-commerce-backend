# Tee tähän oma ValidationError, jota voit käyttää mm. Category-classin create-metodissa.
class ValidationError(Exception):
    def __init__(self, message="Validation Error"):
        self.args = (message,)
