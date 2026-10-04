class Solution:

    def encode(self, strs: List[str]) -> str:
        self.encoded = ""
        self.chara_delimiter = chr(129)
        self.string_delimiter = chr(130)
        for current_string in strs:
            group = ""
            encoded_string = ""
            for chara in current_string:
                if not group or group[-1] == chara:
                    group += chara
                else:
                    encoded_string += f"{group[0]}{self.chara_delimiter}{len(group)}{self.chara_delimiter}"
                    group = chara
            
            if group:
                encoded_string += f"{group[0]}{self.chara_delimiter}{len(group)}{self.chara_delimiter}"
            
            self.encoded += f"{encoded_string}{self.string_delimiter}"
        return self.encoded
    
    def decode(self, s: str) -> List[str]:
        words = s.split(self.string_delimiter)[:-1]
        res = []

        for word in words:
            parts = word.split(self.chara_delimiter)
            decoded = []
            # The last element is always an empty string from the trailing
            # delimiter, so stop one short and step through (char, count) pairs.
            for i in range(0, len(parts) - 1, 2):
                decoded.append(parts[i] * int(parts[i + 1]))
            res.append("".join(decoded))

        return res