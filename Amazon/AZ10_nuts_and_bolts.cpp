class Solution {
public:

	void matchPairs(char nuts[], char bolts[], int n) {
		
		map<char, int> m;
		m['!']++;
		m['#']++;
		m['$']++;
		m['%']++;
		m['&']++;
		m['*']++;
		m['@']++;
		m['^']++;
		m['~']++;

		map<char, int> nutmap;
		map<char, int> boltmap;

		for (int i = 0; i < n ; i++){
			nutmap[nuts[i]]++;
			boltmap[bolts[i]]++;
		}
		int j = 0;
		for (auto i : m){
			if (nutmap.find(i.first) != nutmap.end() && boltmap.find(i.first) != boltmap.end()){
				nuts[j] = i.first;
				bolts[j] = i.first;
				j++;
			}
		}
	}

};