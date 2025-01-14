import logging
from typing import Any, Dict, List, Tuple

from haystack import component

logger = logging.getLogger(__name__)


class Calculator(component):
    """
    A simple calculator node for Haystack.
    """

    outgoing_edges = 1

    def run(self, query: str, **kwargs: Any) -> Tuple[Dict[str, Any], str]:
        """
        Main execution logic of the node.

        :param query: The user query, expected to be a math expression (e.g. "2 + 2")
        :param kwargs: Additional parameters from preceding nodes
        :return: A tuple (output_dict, "output_edge_name")
        """
        expression = query.strip()
        logger.info(f"Received expression for calculation: {expression}")

        try:
            result = eval(expression)
        except Exception as e:
            logger.error(f"Error in evaluating expression '{expression}': {e}")
            result = None

        output = {"result": result}
        return output, "output_1"

    def run_batch(
        self, queries: List[str], **kwargs: Any
    ) -> Tuple[List[Dict[str, Any]], str]:
        """
        Batch processing version of `run`.
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
