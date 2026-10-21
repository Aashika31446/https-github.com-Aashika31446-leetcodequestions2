class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left=0,right=numbers.size()-1;
        while(left<right){
            int sumval=numbers[left]+numbers[right];
            if(sumval==target){
                return {left+1,right+1};
            }
            else if(sumval<target){
                left++;
            }
            else if(sumval>target){
                right--;
            }
        }
        return {};
       
        
    }
      
};