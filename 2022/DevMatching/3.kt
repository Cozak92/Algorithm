//
//class Solution {
//    lateinit var matrix: MutableList<MutableList<Int>>
//    lateinit var answerList: MutableList<MutableList<Int>>
//    lateinit var visit: BooleanArray// 방문 여부 체크
//    var N:Int = 0
//
//    fun dfs(start: Int, end: Int, k: Int, count: Int, path:MutableList<Int>){
//        if(count >= N){
//            return
//        }
//        if(start == end && k >= count){
//            println(path)
//            answerList.add(path)
//            return
//        }
//
//        for(i in 0 until N){
//            if(matrix[start][i] == 1 && !visit[i]){
//                path.add(i)
//                path.dropLast(1)
//                dfs(i, end,k,count+1, path.toMutableList().to)
//            }
//        }
//
//
//
//    }
//
//    fun solution(n: Int, edges: Array<IntArray>, k: Int, a: Int, b: Int): Int {
//        N = n
//        matrix = MutableList(N) { MutableList(N) {0} }
//        for( edge in edges){
//            matrix[edge[0]][edge[1]] = 1
//            matrix[edge[1]][edge[0]] = 1
//        }
//
//        answerList = mutableListOf()
//        var path: MutableList<Int> = mutableListOf()
//        visit = BooleanArray(n)
//        dfs(a,b,k,1, path.toMutableList())
//        var cc = 0
//        for(p in 0 until n){
//            if(!answerList.flatten().contains(p)){
//                cc++
//            }
//        }
//
//
//
//        return n - cc
//    }
//}