class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self,product_name,cost):
        self.product_name=product_name
        self.cost=cost
        self.product_num=0
        self.coin=0

    def vend(self):
        if not self.product_num:
            return f"Inventory empty. Restocking required."
        elif self.coin<self.cost:
            return f"You must add ${self.cost-self.coin} more funds."
        else:
            self.product_num -= 1
            self.coin-=self.cost
            if self.coin:
                temp=self.coin
                self.coin=0
                return f'Here is your {self.product_name} and ${temp} change.'
            else:
                return f"Here is your {self.product_name}."

    def add_funds(self,num):
        if not self.product_num:
            return f'Inventory empty. Restocking required. Here is your ${num}.'
        else:
            self.coin+=num
            return f'Current balance: ${self.coin}'
    def restock(self,num):
        self.product_num+=num
        return f'Current {self.product_name} stock: {self.product_num}'
def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    num = n % 10
    first = Link(num, Link.empty)
    n//=10
    while n:
        first=Link(n%10,first)
        n//=10
    return first

def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    if t.label==value:
        yield [t.label]
    for item in t.branches:
        for x in path_yielder(item,value):
            yield [t.label]+x



class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):

        return kind(self.year)

    def update(self):
        self.year=Mint.current_year


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        return self.cents if Mint.current_year-self.year<50 else self.cents+Mint.current_year-self.year-50


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    def helper_max(t):
        if t.is_leaf():
            return t.label
        else:
            return max(helper_max(t.branches[-1]),t.label)
    def helper_min(t):
        if t.is_leaf():
            return t.label
        else:
            return min(helper_max(t.branches[0]),t.label)
    if t.is_leaf():
        return True
    elif len(t.branches)==1:
        return is_bst(t.branches[0]) and (helper_max(t.branches[0])<=t.label or helper_min(t.branches[0])>=t.label)
    elif len(t.branches)==2:
        return is_bst(t.branches[0]) and is_bst(t.branches[1]) and  helper_max(t.branches[0])<=t.label  and helper_min(t.branches[1])>=t.label
    return False
    # def bst_min(t):
    #     if t.is_leaf(): return t.label
    #     return min(t.label, bst_min(t.branches[0]))
    #
    # def bst_max(t):
    #     if t.is_leaf(): return t.label
    #     return max(t.label, bst_max(t.branches[-1]))
    #
    # if t.is_leaf(): return True
    # if len(t.branches) == 1:
    #     child = t.branches[0]
    #     return is_bst(child) and \
    #         (bst_max(child) <= t.label or bst_min(child) > t.label)
    # elif len(t.branches) == 2:
    #     left_child, right_child = t.branches
    #     return is_bst(left_child) and is_bst(right_child) and \
    #         bst_max(left_child) <= t.label and bst_min(right_child) > t.label
    # else:
    #     return False
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    if t.is_leaf():
        return [t.label]
    else:
        ret=[t.label]
        for item in t.branches:
            ret+=preorder(item)
        return ret



def generate_preorder(t):
    """Yield the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> gen = generate_preorder(numbers)
    >>> next(gen)
    1
    >>> list(gen)
    [2, 3, 4, 5, 6, 7]
    """
    yield t.label
    for item in t.branches:
        yield from generate_preorder(item)


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
