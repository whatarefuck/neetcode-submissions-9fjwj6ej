use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut memory_map: HashMap<i32, i32> = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            memory_map.insert(num, i as i32);
        }
        for (i, &num) in nums.iter().enumerate() {
            if let Some(&j) = memory_map.get(&(target - num)){
                if i as i32 != j{
                    return vec![i as i32, j];
                }
            }
        }
        vec![]
    }
}