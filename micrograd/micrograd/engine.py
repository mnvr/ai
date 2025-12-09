class Value:
    """Store a single scalar value and its gradient."""

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        # Internal variables used for autograd graph construction.
        self._backward = lambda: None
        self._prev = set(_children)
        # The op that produced this node, for graphviz / debugging etc.
        self._op = _op

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += 1 * out.grad
            other.grad += 1 * out.grad
            pass
        out._backward = _backward

        return out
