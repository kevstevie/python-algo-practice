/**
 * Problem: #208 - Implement Trie (Prefix Tree)
 * Difficulty: Medium
 * Language: Kotlin
 * URL: https://leetcode.com/problems/implement-trie-prefix-tree/
 * Submitted: 2026-07-23
 * Tags: Hash Table, String, Design, Trie
 */
class Trie() {
    val root: Node = Node()

    fun insert(word: String) {
        var cur = root
        for(c in word) {
            cur.child.getOrPut(c) { Node() }
            cur = cur.child[c]!!
        }
        cur.isEnd = true
    }

    fun search(word: String): Boolean {
        var cur = root
        for(c in word) {
            cur = cur.child[c] ?: return false
        }
        return cur.isEnd
    }

    fun startsWith(prefix: String): Boolean {
        var cur = root
        for(c in prefix) {
            cur = cur.child[c] ?: return false
        }
        return true
    }

    class Node() {
        val child = mutableMapOf<Char, Node>()
        var isEnd: Boolean = false
    }
}


/**
 * Your Trie object will be instantiated and called as such:
 * var obj = Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
