
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
#include <string>
#include <vector>
#include <iostream>
#include <string.h>
using namespace std;


const int NUM = 27;

int toNumber(char n) {
    if (n == '?')
    {
        return 26;
    }

    return n - 'a';
}

struct TrieNode
{
    TrieNode* children[NUM];
    bool terminal;
    int cnt;

    TrieNode() :terminal(false), cnt(0)
    {
        for (int i = 0; i < NUM; ++i)
        {
            children[i] = NULL;
        }
    }

    ~TrieNode()
    {
        for (int i = 0; i < NUM; i++)
        {
            if (children[i]) 
            {
                delete children[i];
            }
        }
    }

    void insert(const char* key) 
    {
        //키값이 널이라면
        if (*key == 0)
        {
            terminal = true;
        }
        else
        {
            int next = toNumber(*key);
            if (children[next] == NULL)
            {
                children[next] = new TrieNode();
            }

            children[next]->insert(key + 1);
        }
    }

    void find(const char* key) 
    {
        if (*key == 0) 
        {
            cnt++;
            return;
        }

        int next = toNumber(*key);
        if (children[toNumber('?')] != NULL)
        {
            children[toNumber('?')]->find(key + 1);
        }

        if (children[next] != NULL)
        {
            children[next]->find(key + 1);
        }
    }

    int getCnt(const char* key)
    {
        if (*key == 0) 
        {
            return cnt;
        }

        int next = toNumber(*key);
        if (children[next] == NULL)
        {
            return 0;
        }

        return children[next]->getCnt(key + 1);
    }
};

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    TrieNode trie;

    for (int i = 0; i < queries.size(); ++i)
    {
        trie.insert(queries[i].c_str());
    }

    for (int i = 0; i < words.size(); ++i)
    {
        trie.find(words[i].c_str());
    }

    for (int i = 0; i < queries.size(); ++i)
    {
        answer.push_back(trie.getCnt(queries[i].c_str()));
    }

    return answer;
}