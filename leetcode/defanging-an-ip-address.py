# defanging-an-ip-address.py
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


sol = Solution()
address = "192.168.224.24"
print(sol.defangIPaddr(address))
