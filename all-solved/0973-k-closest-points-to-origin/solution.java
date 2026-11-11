import java.util.PriorityQueue;

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>(
            (a, b) -> Integer.compare(
                a[0] * a[0] + a[1] * a[1],
                b[0] * b[0] + b[1] * b[1]
            )
        );
        int[][] result = new int[k][2];

        for (int[] point : points) {
            heap.offer(point);
        }

        for (int i = 0; i < k; i++) {
            result[i] = heap.poll();
        }

        return result;
    }
}
