"""
From geek for geeks.

To be understood and debugged

"""
void diagonalPrintUtil(Node* root, int d,
                      map<int, vector<int>> &diagonalPrint)
{
    if (!root)
        return;
 
    diagonalPrint[d].push_back(root->data);
 
    // Increase the vertical distance if left child
    diagonalPrintUtil(root->left, d + 1, diagonalPrint);
 
    // Vertical distance remains same for right child
    diagonalPrintUtil(root->right, d, diagonalPrint);
}
 
// Print diagonal traversal of given binary tree
void diagonalPrint(Node* root)
{
    // create a map of vectors to store Diagonal elements
    map<int, vector<int> > diagonalPrint;
    diagonalPrintUtil(root, 0, diagonalPrint);
 
    cout << "Diagonal Traversal of binary tree : \n";
    for (auto it = diagonalPrint.begin();
         it != diagonalPrint.end(); ++it)
    {
        for (auto itr = it->second.begin();
             itr != it->second.end(); ++itr)
            cout << *itr  << ' ';
 
        cout << '\n';
    }
}
