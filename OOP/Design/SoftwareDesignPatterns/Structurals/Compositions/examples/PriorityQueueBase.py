class PriorityQueueBase:
    """Abstract base class for a priority queue."""
    class Item:
        """Lightweight composite to store priority queue items."""
        slots = '_key ', '_value'
        def __init__ (self, k, v):
            self. key = k
            self. value = v