from haystack import component

class Calculator(component):

    def run(self, query: str, **kwargs):
        try:
            result = eval(query)
        except Exception as e:
            result = None
        return {"result": result}
