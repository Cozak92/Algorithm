import java.util.*


var N = 0
var M = 0
var count = 0
lateinit var graph: Array<IntArray> // 무방향 그래프
lateinit var visit: BooleanArray // 방문 여부 체크
fun dfs(i: Int) {
    visit[i] = true
    for (j in 1..N) {
        if (graph[i][j] == 1 && !visit[j]) {
            dfs(j)
        }
    }
}


fun main(args: Array<String>) {
    val scan = Scanner(System.`in`)
    N = scan.nextInt()
    M = scan.nextInt()
    graph = Array(N + 1) { IntArray(N + 1) }
    visit = BooleanArray(N + 1)
    for (i in 1..M) {
        val a = scan.nextInt()
        val b = scan.nextInt()
        graph[b][a] = 1
        graph[a][b] = graph[b][a]
    }
    for (i in 1..N) {
        if (!visit[i]) {
            dfs(i)
            count++
        }
    }
    println(count)
    scan.close()
}
