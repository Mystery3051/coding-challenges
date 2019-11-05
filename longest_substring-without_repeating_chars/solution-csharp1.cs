using System;

public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        if (s == null)
            throw new Exception("Null string");

        if (s == "")
            return 0;

        Dictionary<char, int> maxSubstring = new Dictionary<char, int>();
        maxSubstring.Add(s[0], 0);
        int maxlen = 1;
        int lastMaxLen = 0;
        for (int i = 1; i < s.Length; i++)
        {
            if (maxSubstring.ContainsKey(s[i]))
            {
                if (maxlen > lastMaxLen)
                    lastMaxLen = maxlen;

                int charPosition = maxSubstring[s[i]];
                foreach (var keyValues in maxSubstring.Where(kvp =>
                                            (kvp.Value < charPosition)).ToList())
                {
                    maxSubstring.Remove(keyValues.Key);
                    maxlen--;
                }
                maxSubstring[s[i]] = i;
            }
            else
            {
                maxSubstring.Add(s[i], i);
                maxlen++;
            }
        }

        return Math.Max(maxlen, lastMaxLen);
    }
}
