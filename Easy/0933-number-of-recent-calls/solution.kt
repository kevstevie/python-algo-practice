/**
 * Problem: #933 - Number of Recent Calls
 * Difficulty: Easy
 * Language: Kotlin
 * URL: https://leetcode.com/problems/number-of-recent-calls/
 * Submitted: 2026-07-23
 * Tags: Design, Queue, Data Stream
 */
class RecentCounter() {
    val q: Queue<Int> = LinkedList()

    fun ping(t: Int): Int {
        while (q.isNotEmpty() && q.peek() < t - 3000) {
            q.poll()
        }
        q.offer(t)
        return q.size
    }

}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = RecentCounter()
 * var param_1 = obj.ping(t)
 */
