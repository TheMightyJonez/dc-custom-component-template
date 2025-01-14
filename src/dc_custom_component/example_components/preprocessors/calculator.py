from haystack.nodes import Component

class Calculator(Component):

    def run(self, query: str, **kwargs):
        try:
            result = eval(query)
        except Exception as e:
            result = None
        return {"result": result}, "output_1"
