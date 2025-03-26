class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split(" ")

        filtered_words = []
        for word in words:
            if word != "":
                filtered_words.append(word)
        filtered_words.reverse()
        result = " ".join(filtered_words)
        return result