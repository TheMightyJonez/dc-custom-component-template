from haystack.nodes import Component

class Calculator(Component):
    def __init__(self):
        super().__init__()

    def run(self, query: str, **kwargs):
        try:
            result = eval(query)
        except Exception as e:
            result = None
        return {"result": result}, "output_1"

    def to_dict(self):
        return {"type": self.__class__.__name__}
