from haystack.nodes import Component  # or 'from haystack.preview.components import Component' depending on your version

class Calculator(Component):
    def __init__(self, param1=None, param2=None):
        # IMPORTANT: The new Component class doesn't expect positional arguments.
        # Always call super().__init__() with no extra arguments:
        super().__init__()
        
        # Store custom parameters as instance variables, if needed:
        self.param1 = param1
        self.param2 = param2

    def run(self, query: str, **kwargs):
        # Your custom logic. For example:
        try:
            result = eval(query)
        except Exception as e:
            result = None
        
        return {"result": result}, "output_1"

    def to_dict(self):
        """
        The to_dict() method is needed if you load/save pipelines from YAML or
        use the new pipeline "config" approach. It tells Haystack how to re-instantiate
        this component.

        Make sure your keys match any custom arguments in __init__().
        """
        return {
            "type": self.__class__.__name__,
            "param1": self.param1,
            "param2": self.param2
        }
