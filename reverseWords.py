#151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        arr1 = []
        cleaned_text = re.sub(r'\s+', ' ', s)
        cleaned_text = cleaned_text.strip()
        for word in cleaned_text.split(" "):
                arr1.append(word)
        arr1.reverse()
        return " ".join(arr1)
