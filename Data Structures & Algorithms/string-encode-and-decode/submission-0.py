class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            ans += s
            ans += "—"
        
        return ans

    def decode(self, s: str) -> List[str]:

        ans = s.split("—")

        return ans[0:len(ans)-1]
