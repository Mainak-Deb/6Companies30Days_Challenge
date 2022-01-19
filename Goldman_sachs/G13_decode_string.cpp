class Solution{
    string breakcode(string &str, int &m)
    {
        string result;
        while (m < str.length() && str[m] != ']')
        {
            if (isdigit(str[m])) 
            {
                int k = 0;
                while (m < str.length() && isdigit(str[m])) 
                {
                    k = k * 10 + (str[m] - '0');
                    m++;
                }

                m++; 
                string rem = breakcode(str, m); 
                while (k > 0) 
                {
                    result += rem;
                    k--;
                }
                m++; 
            }
            else
            {
                result.push_back(str[m++]); 
            }
        }
        return result;
    }

public:
    string decodedString(string s) {
        int i = 0;
        return breakcode(s, i);
    }
};