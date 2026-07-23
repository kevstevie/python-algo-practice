/**
 * Problem: #900 - RLE Iterator
 * Difficulty: Medium
 * Language: Kotlin
 * URL: https://leetcode.com/problems/rle-iterator/
 * Submitted: 2026-07-23
 * Tags: Array, Design, Counting, Iterator
 */
class RLEIterator(encoding: IntArray) {
    val encoding:IntArray = encoding
    var idx:Int = 0

    fun next(n: Int): Int {
        var cur = n
        if (idx >= encoding.size) {
            return -1
        }
        while (cur != 0) {
            while (encoding[idx] == 0) {
                idx += 2
                if (idx >= encoding.size) {
                    return -1
                }
            }
            val sub = min(cur, encoding[idx])
            cur -= sub
            encoding[idx] -= sub
        }
        return encoding[idx + 1]
    }

}

/**
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = RLEIterator(encoding)
 * var param_1 = obj.next(n)
 */
