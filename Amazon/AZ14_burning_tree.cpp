
class Solution14 {
public:
    int minTime(Node* root, int target)
    {
        unordered_map <Node*, Node*> parent;
        unordered_map <Node*, bool> visited;
        queue<Node*> q;
        int time = 0;
        q.push(root);
        Node * trgt;
        while (!q.empty()){
            int n = q.size();
            while (n--){
                Node *temp = q.front();
                q.pop();
                if (temp -> data == target){
                    trgt = temp;
                }
                if (temp->left != NULL){
                    q.push(temp->left);
                    parent[temp->left] = temp;
                }
                if (temp->right != NULL){
                    q.push(temp->right);
                    parent[temp->right] = temp;
                }
            }
        }
        q.push(trgt);
        visited[trgt] = true;
        while (!q.empty()){
            int n = q.size();
            while (n--){
                Node * temp = q.front();
                q.pop();
                if (temp -> left != NULL && visited[temp->left] == false){
                    q.push(temp->left);
                    visited[temp->left] = true;
                }
                if (temp -> right != NULL && visited[temp->right] == false){
                    q.push(temp->right);
                    visited[temp->right] = true;
                }
                if (parent[temp] != NULL && visited[parent[temp]] == false){
                    q.push(parent[temp]);
                    visited[parent[temp]] = true;
                }
            }
            time++;
        }
        return time - 1;
    }
};