class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]

        ans = { "".join(morse[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(ans)