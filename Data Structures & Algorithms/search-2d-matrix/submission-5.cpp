class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left = 0;
        int right = (matrix.size()*matrix[0].size())-1;
        int rsize = (matrix[0].size());

        while (left <= right){
            int mid = (left+right)/2;
            int i = mid/rsize;
            int j = mid - i*rsize;
            if (target == matrix[i][j]){
                return true;
            } else if (target > matrix[i][j]){
                left = mid + 1;
            } else if (target < matrix[i][j]){
                right = mid - 1;
            }
        }
        return false;
    }
};
