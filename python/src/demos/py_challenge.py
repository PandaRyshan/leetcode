# -- coding: utf-8 --

import urllib.request
import re
import pickle

from collections import Counter


class Challenge:

    def problem_2(self):
        """http://www.pythonchallenge.com/pc/def/ocr.html
        """
        url = "http://www.pythonchallenge.com/pc/def/ocr.html"
        html = urllib.request.urlopen(url).read().decode()

        message = re.findall(r"<!--(.*?)-->", html, re.DOTALL)[-1]
        counter = Counter(message)
        answer = ''.join([char for char in message if counter[char] < 10])
        print(answer)

    def problem_3(self):
        """http://www.pythonchallenge.com/pc/def/equality.html
        """
        url = "http://www.pythonchallenge.com/pc/def/equality.html"
        html = urllib.request.urlopen(url).read().decode()

        message = re.findall(r"<!--(.*?)-->", html, re.DOTALL)[-1]
        message = re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", message)
        print(message)

    def problem_4(self):
        """http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
        """
        base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
        url = base_url % "95493"

        num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

        symbol_pattern = re.compile(r'\bplus\b|\bminus\b|\bdivide\b|\btimes\b',
                                    re.IGNORECASE)
        num_pattern = re.compile(
            r'\b(zero|one|two|three|four|five|six|seven|eight|nine)\b',
            re.IGNORECASE)

        for _ in range(400 - 1):
            html = urllib.request.urlopen(url).read().decode()
            print(html)
            args = re.findall(r"nothing is (\d+)", html)
            if not args:
                original_num = int(re.findall(r"nothing=(\d+)", url)[0])
                symbol = re.search(symbol_pattern, html).group()
                num = int(num_dict[re.search(num_pattern, html).group()])
                if symbol.lower() == 'plus':
                    original_num += num
                elif symbol.lower() == 'minus':
                    original_num -= num
                elif symbol.lower() == 'divide':
                    original_num //= num
                elif symbol.lower() == 'times':
                    original_num *= num
                args.append(original_num)
            url = base_url % args[0]

    def problem_5(self):
        handle = urllib.request.urlopen(
            "http://www.pythonchallenge.com/pc/def/banner.p")
        data = pickle.load(handle)
        handle.close()
        print(data)
        for line in data:
            print(''.join([char * num for char, num in line]))


if __name__ == "__main__":
    Challenge().problem_5()
