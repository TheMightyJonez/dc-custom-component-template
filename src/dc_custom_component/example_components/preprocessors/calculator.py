import logging
from haystack import BaseComponent

logger = logging.getLogger(__name__)

class Calculator(BaseComponent):
    """
    A simple calculator node for Haystack.

    This node parses the query as a math expression and evaluates its result.
    """

    # Haystack 1.x uses outgoing_edges to describe how many output edges
    # your component has. Typically 1 for standard nodes.
    outgoing_edges = 1

    def run(self, query: str, **kwargs):
        """
        Main execution logic of the node.

        :param query: The user query, expected to be a math expression (e.g. "2 + 2")
        :param kwargs: Unused additional parameters
        :return: A dict that contains the result of the calculation
        """

        # Step 1: Optionally sanitize or parse the query here
        expression = query.strip()
        logger.info(f"Received expression for calculation: {expression}")

        # Step 2: Try to evaluate the expression
        try:
            result = eval(expression)
        except Exception as e:
            logger.error(f"Error in evaluating expression '{expression}': {e}")
            result = None

        # The "output" key can be used to pass on data to subsequent nodes
        output = {"result": result}

        # Return value must be a tuple: (dict_with_outputs, "name_of_output_edge")
        # By default, you can return ("output_1") if there is only one outgoing edge.
        return output, "output_1"

    def run_batch(self, queries, **kwargs):
        """
        (Optional) Batch processing version of `run`.
        If you need to process queries in batch for efficiency, implement your logic here.
        """
        results = []
        for query in queries:
            expression = query.strip()
            try:
                result = eval(expression)
            except Exception as e:
                logger.error(f"Error in evaluating expression '{expression}': {e}")
                result = None
            results.append({"result": result})

        return results, "output_1"
