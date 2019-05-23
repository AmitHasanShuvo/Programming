class Solution(object):
    def numUniqueEmails(self, emails):
        actual = set()
        for email in emails:
            x = email.split("@")
            y = x[0].split("+")
            z = y[0].replace(".","")
            x = z + "@" + x[1]
            actual.add(c)
            return len(actual)
