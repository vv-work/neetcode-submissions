class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var countS = [Character: Int]() 
        for c in s{
            countS[c, default: 0] += 1

        }
        for c in t {
            if (countS[c,default:0]<=0){
                return false
            }
            else{
                countS[c, default:0] -= 1 
            }

        }
        for (k,v) in countS{
            if (v != 0) {
                return false
            }
        }
        return true 
    }
}
