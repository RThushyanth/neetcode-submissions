
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int ans = std::ranges::max(piles);
        int left = 1;
        int right = std::ranges::max(piles);

        while (left<=right){
            int mid = (left+right)/2;
            int time = 0;
            for (int i=0;i<piles.size();i++){
                time += (piles[i]+mid-1)/mid;
            }
            if (time<=h){
                ans = std::min(ans,mid);
                right = mid-1;
            } else if (time>h){
                left = mid+1;

            }
        }
        return ans;
    }   
};
