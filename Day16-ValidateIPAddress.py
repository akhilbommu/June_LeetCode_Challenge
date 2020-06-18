"""
https://leetcode.com/problems/validate-ip-address/
"""


class ValidateIPAddress:
    def validIPAddress(self, IP):
        if "." in IP:
            split_list = IP.split(".")
            if len(split_list) != 4:
                return "Neither"
            for part in split_list:
                if len(part) == 0 or (len(part) > 1 and part[0] == "0"):
                    return "Neither"
                if not part.isnumeric() or int(part) > 255:
                    return "Neither"
            return "IPv4"
        elif ":" in IP:
            symbols = "0123456789abcdefABCDEF"
            split_list = IP.split(":")
            if len(split_list) != 8:
                return "Neither"
            for part in split_list:
                if len(part) == 0 or len(part) > 4:
                    return "Neither"
                for elem in part:
                    if elem not in symbols:
                        return "Neither"
            return "IPv6"
        return "Neither"


obj = ValidateIPAddress()
print(obj.validIPAddress("172.16.254.1"))
print(obj.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(obj.validIPAddress("256.256.256.256"))
print(obj.validIPAddress("3204989084338912748932647812689708923sdjlkch9 i389273012380009832437218947389-7534iodu"))
