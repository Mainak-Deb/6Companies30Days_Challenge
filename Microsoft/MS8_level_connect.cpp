class Solution
{
public:
    //Function to connect nodes at same level.
    void connect(Node *root)
    {
       
        root->nextRight = NULL;
        queue<Node*> q;
        q.push(root);
        vector<Node*> levelorder;
        vector<int> number;
        while (!q.empty())
        {
            int k = q.size();
            number.push_back(k);
            while (k--)
            {
                Node * start = q.front();
                levelorder.push_back(start);
                q.pop();
                if (start -> left != NULL)
                {
                    q.push(start->left);
                }
                if (start -> right != NULL)
                {
                    q.push(start -> right);
                }
            }
        }

        int index = 0;
        for (int i = 0; i < number.size(); i++)
        {
            while (number[i] != 0)
            {
                if (number[i] == 1)
                {
                    levelorder[index] -> nextRight = NULL;
                }
                else
                {
                    levelorder[index] -> nextRight = levelorder[index + 1];
                }
                index++;
                number[i]--;
            }
        }
    }

};


