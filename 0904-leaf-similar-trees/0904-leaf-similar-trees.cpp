/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void Totalleaves(TreeNode* node, vector<int>& leaves) {
        if(node==nullptr){
            return;
        }
        if(node->left==nullptr && node->right==nullptr){
            leaves.push_back(node->val);
        }
        Totalleaves(node->left,leaves);
        Totalleaves(node->right,leaves);
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int>leaves1,leaves2;
        Totalleaves(root1,leaves1);
        Totalleaves(root2,leaves2);
        
        return leaves1==leaves2;
    }
};