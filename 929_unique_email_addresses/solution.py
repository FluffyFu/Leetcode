from typing import List


class Solution:
    def num_unique_emails(self, emails: List[str]) -> int:
        email_set = set()
        for s in emails:
            clean_s = ''
            for i, c in enumerate(s):
                if c == '@':
                    clean_s += s[i:]
                    break
                elif c == '.':
                    pass
                elif c == '+':
                    j = i
                    while s[j] != '@':
                        j += 1
                    clean_s += s[j:]
                    break
                else:
                    clean_s += c
            email_set.add(clean_s)

        return len(email_set)

    def num_unique_emails_clean(self, emails: List[str]) -> str:
        seen = set()
        for email in emails:
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.', '')
            seen.add(name + '@' + domain)

        return len(seen)
