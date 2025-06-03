# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahren = celsius * 1.80 +32.00
        list_of_temp = [kelvin,fahren]
        return list_of_temp

        