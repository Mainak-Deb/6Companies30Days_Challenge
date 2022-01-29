
template <typename T>
class Graph {


	map<T, list<T>> l;


public:


	void addEdge(T x , T y)
	{
		l[x].push_back(y);
	}

	string topological_sort()
	{
		//calculate the indegree for each of the node
		map<T, int> indegree;
		string answer = "";
		for (auto i : l)
		{
			indegree[i.first] = 0;
		}
		for (auto i : l)
		{
			for (auto j : l[i.first])
			{
				//if (j != "NULL")
				indegree[j]++;
			}
		}
// 		vector<T> result;
		queue<T> s;
		for (auto i : l)
		{
			if (indegree[i.first] == 0)
			{
				s.push(i.first);
			}
		}
		while (!s.empty())
		{
			T node = s.front();
			s.pop();
			//result.push_back(node);
			answer.push_back(node);
			for (auto i : l[node])
			{
				indegree[i]--;
				if (indegree[i] == 0)
				{
					s.push(i);
				}
			}
		}

		return answer;

	}


};

class Solution {
public:
	string findOrder(string dict[], int N, int K) {
		//code here
		int i, j, k;
		Graph<char> g;
		for (i = 1; i < N; i++)
		{
			string s1 = dict[i - 1],s2 = dict[i];
			for (j = 0; j < min(s1.size(), s2.size()) ; j++){
				if (s1[j] != s2[j]){g.addEdge(s1[j], s2[j]);break;}
		    }
		}
		string answer = g.topological_sort();
		return answer;
	}
};