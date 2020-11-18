# unique-email-addresses.py
'''
ちょっと面倒な処理が書けますか + set 使えますかという問題
'''


class Solution:
    def numUniqueEmails(self, emails) -> int:
        uniqueMails = set()
        for email in emails:
            local, domain = email.split('@')
            local, *_ = local.split('+')
            local = local.replace('.', '')
            uniqueMails.add(local+'@'+domain)
        return len(uniqueMails)
