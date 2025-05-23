class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        long long baseSum = 0;
        vector<long long> gains;

        for (int num : nums) {
            baseSum += num;
            long long toggled = num ^ k;
            gains.push_back(toggled - num); // how much gain we get if we flip this node
        }

        // Sort the gains in decreasing order
        sort(gains.rbegin(), gains.rend());

        // We want to pick even number of operations (edges affect 2 nodes)
        long long totalGain = 0;
        int i = 0;
        while (i + 1 < gains.size() && gains[i] + gains[i + 1] > 0) {
            totalGain += gains[i] + gains[i + 1];
            i += 2;
        }

        return baseSum + totalGain;
    }
};
