try:
    from .add import add
    from .division import division
    from .minus import minus
    from .multi import multi as multiplication
except ImportError:
    from add import add
    from division import division
    from minus import minus
    from multi import multi as multiplication

__all__ = ["add", "minus", "multiplication", "division"]
