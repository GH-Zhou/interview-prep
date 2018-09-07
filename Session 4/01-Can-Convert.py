import unittest
import collections

Rate = collections.namedtuple('Rate', ('currency_from', 'currency_to'))

# ---- Assumptions
#      1. Since we don't need to return the actual rate for the input, we don't need to store or fetch the
#      rate figures for each currency conversion.

# ---- Test Cases
#   Given rates: [(USD, CNY), (CNY, MYR), (EUR, USD), (JPY, KRW)]
#   1) Input: (CNY, EUR)        Output: True
#   2) Input: (USD, MYR)        Output: True
#   3) Input: (USD, KRW)        Output: False
#   4) Input: (KRW, JPY)        Output: True
#   5) Input: (CNY, USD)        Output: True

# ---- Approach 1 (DFS)
# Idea: Given the rates, we can turn them into a undirected graph, and look for the connected components,
#       for each pair of the currencies in each component they can be converted mutually. Then we can check
#       if the sink currency_to is reachable from the source (currency_from).
#
# Implementation:

given_rates = [Rate('USD', 'CNY'), Rate('CNY', 'MYR'), Rate('EUR', 'USD'), Rate('JPY', 'KRW')]
def generate_graph(rates):

    graph = collections.defaultdict(list)

    for rate in rates:
        graph[rate.currency_from].append(rate.currency_to)
        graph[rate.currency_to].append(rate.currency_from)

    return graph

def canConvert_1(currency_from, currency_to):
    graph = generate_graph(given_rates)
    visited = set()

    def dfs(cur_currency):
        if cur_currency in visited:
            return False
        visited.add(cur_currency)

        if cur_currency == currency_to:
            return True
        if any(map(dfs, [next_currency for next_currency in graph[cur_currency]])):
            return True
        return False

    return dfs(currency_from)
# ---- Complexity
#   Time:  O(|V| + |E|), where |V| is the number of currencies, and |E| is the length of the given rates
#   Space: O(|V|), spent on the call stack and visited set

# ---- Approach 2 (BFS)
# Idea: Same idea as approach 1, but use BFS instead
#
# Implementation:
def canConvert_2(currency_from, currency_to):
    graph = generate_graph(given_rates)
    visited = set()

    q = collections.deque([currency_from])
    while q:
        cur_currency = q.popleft()
        visited.add(cur_currency)
        for next_currency in graph[cur_currency]:
            if next_currency not in visited:
                if next_currency == currency_to:
                    return True
                q.append(next_currency)

    return False
# ---- Complexity
#   Time:  O(|V| + |E|), where |V| is the number of currencies, and |E| is the length of the given rates
#   Space: O(|V|), spent on the queue and visited set

class TestCanConvert(unittest.TestCase):

    def test_can_convert_1(self):
        self.assertTrue(canConvert_1('CNY', 'EUR'))
        self.assertTrue(canConvert_1('USD', 'MYR'))
        self.assertFalse(canConvert_1('USD', 'KRW'))
        self.assertTrue(canConvert_1('KRW', 'JPY'))
        self.assertTrue(canConvert_1('CNY', 'USD'))
        self.assertFalse(canConvert_1('JPY', 'USD'))

    def test_can_convert_2(self):
        self.assertTrue(canConvert_2('CNY', 'EUR'))
        self.assertTrue(canConvert_2('USD', 'MYR'))
        self.assertFalse(canConvert_2('USD', 'KRW'))
        self.assertTrue(canConvert_2('KRW', 'JPY'))
        self.assertTrue(canConvert_2('CNY', 'USD'))
        self.assertFalse(canConvert_2('JPY', 'USD'))