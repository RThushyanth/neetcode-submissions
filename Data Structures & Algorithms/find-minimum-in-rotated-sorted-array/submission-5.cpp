class Solution {
public:
    int findMin(vector<int> &nums) {
        if(nums[nums.size()-1]>nums[0]){
            return nums[0];
        }

        int left = 0;
        int right = nums.size()-1;
        int ans = nums[0];
        while (left<right && right-left >=2){
            int mid = (left+right)/2;
            ans = std::min(ans,nums[mid]);
            if(nums[mid]>nums[left]){
                if (nums[mid+1] < nums[mid]){
                    return nums[mid+1];
                }
                left = mid + 1;
            } else if(nums[mid]<nums[right]){
                if (nums[mid-1]>nums[mid]){
                    return nums[mid];
                }
                right = mid -1;
            }
        }
        ans = std::min(ans,std::min(nums[right],nums[left]));

        return ans;
    }   
};
