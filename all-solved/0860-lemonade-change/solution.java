import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean lemonadeChange(int[] bills) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int n : new int[]{5, 10, 20}) {
            map.put(n, 0);
        }

        for (int n : bills) {
            int fives = map.get(5);
            int tens = map.get(10);
            int twenties = map.get(20);

            if (n == 10) {
                if (fives >= 1) {
                    map.put(5, fives - 1);
                    map.put(10, tens + 1);
                } else {
                    return false;
                }
            } else if (n == 20) {
                if (tens >= 1 && fives >= 1) {
                    map.put(5, fives - 1);
                    map.put(10, tens - 1);
                    map.put(20, twenties + 1);
                } else if (fives >= 3) {
                    map.put(5, fives - 3);
                    map.put(20, twenties + 1);
                } else {
                    return false;
                }
            } else {
                map.put(5, fives + 1);
            }
        }

        return true;
    }
}
