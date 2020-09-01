# unique-email-addresses.py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueMails = set()
        for email in emails:
            local,domain = email.split('@')
            local ,*_ = local.split('+')
            local = local.replace('.','')
            uniqueMails.add(local+'@'+domain)
        return len(uniqueMails)
