class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        // nums.count 
        // var unique: Set<int> = []
        // var visited = Set<String>() 
        // visited.conttains(num)
        // `Int` `String`
        var seen: Set<Int> = []
        for num in nums{
            if seen.contains(num){
                return true
            }

            seen.insert(num)

        }
        return false

    }
}
