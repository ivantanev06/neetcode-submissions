class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string  = ""
        for string in strs:
            encoded_string = encoded_string + str(len(string)) + "%" + string 
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        reading = False
        reading_length = 0
        read_index_start = 0
        reading_length_str = []
        index = 0

        while index < len(s):
            if (s[index] != "%"):
                reading_length_str.append(s[index])
                index += 1
            else:
                reading_length = int("".join(reading_length_str))
                reading_length_str = []
                reading_index_start = index + 1
                index = index + reading_length + 1
                new_str = []
                for r in range(reading_length):
                    new_str.append(s[reading_index_start + r])
                new_str = "".join(new_str)
                decoded_strs.append(new_str)
        return decoded_strs

        
        


                    


