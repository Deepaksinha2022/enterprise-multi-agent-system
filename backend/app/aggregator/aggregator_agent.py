from typing import List, Tuple

class AggregatorAgent:

    def aggregate(self, responses: List[Tuple[str, float]]) -> str:

        responses.sort(key=lambda x: x[1], reverse=True)

        return responses[0][0]
    
# dict.fromkeys() removes duplicates while preserving insertion 
# order, unlike set(), which removes duplicates but does not 
# guarantee order.