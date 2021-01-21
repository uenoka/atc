# destination-city.py
'''
普通にdict みたいな1対1のデータ構造でできるけど、結構こんがらがる。
添え字とかこういうのとか結構苦手。
'''
class Solution:
    def destCity(self, paths) -> str:
        route = {}
        for fromCity,toCity in paths:
            route[fromCity] = toCity

        for path in route:
            current = route[path]
            if not current in route:
                return current



sol = Solution()
path =  [["New York","Lima"],["London","New York"],["Lima","Sao Paulo"]]
print(sol.destCity(path))