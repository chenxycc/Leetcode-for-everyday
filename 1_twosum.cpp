class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        vector<int> result;
        for(int i=0; i <nums.size(); i++){
            m[nums[i]]=i;
        }
        for(int i = 0;i <nums.size(); i++){
            int n = target - nums[i];
            if(m.count(n) && m[n] != i){
                result.push_back(i);
                result.push_back(m[n]);
                break;
            }
        }
        return result;
        
        
    }
};