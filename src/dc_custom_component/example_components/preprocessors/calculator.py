from haystack import component
@component
class Calculator:

    def run(self, query: str, **kwargs):
        try:
            result = eval(query)
        except Exception as e:
            result = None
        return {"answers": result}
