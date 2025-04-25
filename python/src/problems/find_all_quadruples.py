# find all quadruples (a, b, c, d) such that
# a^3 + b^3 = c^3 + d^3, all are in [0, 1000]


n = 1000 + 1


class Solution:
    def list_ab_pair(self):
        result_map = {}
        for a in range(n):
            for b in range(n):
                result = a ** 3 + b ** 3
                result_map[result] = (a, b)
        return result_map

    def print_all(self):
        result_map = self.list_ab_pair()
        for c in range(n):
            for d in range(n):
                result = c ** 3 + d ** 3
                if result in result_map:
                    a, b = result_map[result]
                    print(a, b, c, d)


solution = Solution()
solution.print_all()
