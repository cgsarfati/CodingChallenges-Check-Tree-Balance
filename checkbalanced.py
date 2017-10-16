"""Is the tree at this node balanced?

To make this a bit more readable, let's alias our class name:

    >>> N = BinaryNode

For a tree of 1 item:

    >>> tree1 = N(1)
    >>> tree1.is_balanced()
    True

For a tree of 2 items:

  1
 /
2

    >>> tree2 = N(1,
    ...           N(2))
    >>> tree2.is_balanced()
    True

Three:

  1
 / \
2   3

    >>> tree3 = N(1,
    ...           N(2), N(3))
    >>> tree3.is_balanced()
    True

Four:

     1
    / \
   2   4
  /
 3

    >>> tree4 = N(1,
    ...           N(2,
    ...             N(3)),
    ...           N(4))
    >>> tree4.is_balanced()
    True

Five:

     1
   /---\
  2     5
 / \
3   4

    >>> tree5 = N(1,
    ...           N(2,
    ...             N(3), N(4)),
    ...           N(5))
    >>> tree5.is_balanced()
    True

Imbalanced Four:

    1
   /
  2
 / \
3   4

    >>> tree4i = N(1,
    ...            N(2,
    ...              N(3), N(4)))
    >>> tree4i.is_balanced()
    False

Imbalanced Six:

    1
   / \
  2   6
 / \
3   4
   /
  5

    >>> tree6i = N(1,
    ...         N(2,
    ...       N(3), N(4,
    ...           N(5))),
    ...                   N(6))
    >>> tree6i.is_balanced()
    False
"""


class BinaryNode(object):
    """Node in a binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def is_balanced(self):
        """Is the tree at this node balanced?"""

        # balanced if depth from ancestor to leafs differ by no more than 1
        # considerations: traverse from ancestor to leafs, keep count.
        # also need to keep track of L/R traversal. need to compare max height
        # of L and R paths.

        def num_descendants(node):
            """Returns # of descendants. Return None if already imbalanced."""

            # BASE: not a node
            if not node:
                return 0

            # Recurse. Get descendants on left. Fail fast.
            left = num_descendants(node.left)

            if left is None:
                return None

            # Recurse. Get descendents on right. Fail fast.
            right = num_descendants(node.right)

            if right is None:
                return None

            # If heights vary by > 1, imbalanced.
            if abs(left - right) > 1:
                return None

            # If none of above applies, store height of deepest descendant + ourselves
            return max(left, right) + 1

        # Initiate traversal
        return num_descendants(self) is not None

    def is_balanced_ValueError(self):
        """Value error soln vs. passing up None on recursive call stack."""

        def _num_descendants(node):
            """Returns # of descendants. Return None if already imbalanced."""

            # Recurse. Get descendants on left. May raise exception.
            left = _num_descendants(node.left)

            # Recurse. Get descendents on right. May raise exception.
            right = _num_descendants(node.right)

            # If heights vary by > 1, imbalanced. Raise value error vs.
                # passing up None in recursive call stack
            if abs(left - right) > 1:
                raise ValueError()

        try:
            _num_descendants(self)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED! GO GO GO!\n"
