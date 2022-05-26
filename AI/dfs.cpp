#include <bits/stdc++.h> 
using namespace std;


class graph{
public:
map<int,bool>visited;
map<int,list<int> >adj;

void addEdge(int v,int w);
void dfs(int v);
};

void graph::addEdge(int v,int w){
adj[v].push_back(w);
}


void graph:: dfs(int v){
visited[v]=true;
cout<<v<<" ";
list<int>::iterator i;

for(i=adj[v].begin();i!=adj[v].end();i++)
{
	if(!visited[*i])
	{
		dfs(*i);
	}

}
}
int main(){
	graph g;
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEdge(1, 2);
	g.addEdge(2, 0);
	g.addEdge(2, 3);
	g.addEdge(3, 3);
	g.dfs(0);
	cout<<endl;
}

