class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        note = set(ransomNote)

        for i in note:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
