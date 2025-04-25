# 首先，我们将实现一个简单的 Trie 类和 KMP 算法，然后使用它们来解决过滤字符串的问题。
# 接着，我们将生成一些测试用例，运行这两种算法，并测量它们的执行时间和内存使用情况。

import time
from collections import defaultdict
import sys
import tracemalloc

# 实现 Trie 树
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# KMP 算法实现
def KMP_search(pat, txt):
    M = len(pat)
    N = len(txt)

    # 创建 lps[] 以保存最长前缀后缀的长度
    lps = [0]*M
    j = 0 # 模式的索引

    # 计算 lps[] 数组
    computeLPSArray(pat, M, lps)

    i = 0 # 文本的索引
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            return True # 找到模式在文本中的索引为 i-j
            j = lps[j-1]

        # 匹配失败后的处理
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return False

def computeLPSArray(pat, M, lps):
    len = 0 # lps[0] 总是 0

    lps[0] = 0
    i = 1

    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

# 生成测试用例
filter_list = ["foo", "bar", "test", "example", "sample"]
test_strings = ["This is a foo bar test.", "An example string.", "A sample test.", "No keywords here."]

# 初始化 Trie 树并插入过滤列表
trie = Trie()
for word in filter_list:
    trie.insert(word)

# 测试并测量 Trie 和 KMP 的时间和内存使用
tracemalloc.start()

start_time = time.time()
for string in test_strings:
    for word in filter_list:
        trie.search(string)
trie_time = time.time() - start_time
trie_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start_time = time.time()
for string in test_strings:
    for word in filter_list:
        KMP_search(word, string)
kmp_time = time.time() - start_time
kmp_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

(trie_time, trie_memory, kmp_time, kmp_memory)

