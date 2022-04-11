package Baekjoon.사내스터디.`6주차`

object Baekjoon16987 {

    val weight = IntArray(8)
    val durability = IntArray(8)
    var n = 0
    var answer = 0
    fun solve(index: Int) {
        if (index >= n) {
            var cnt = 0
            for (i in 0 until n) {
                if (durability[i] <= 0) cnt++
            }
            answer = if (answer < cnt) cnt else answer
            return
        }
        if (durability[index] <= 0) solve(index + 1);
        else {
            var flag = false;        // 내려쳤는지 안쳤는지 판단
            for (i in 0 until n) {
                if (i == index || durability[i] <= 0) continue;

                durability[index] = durability[index] - weight[i];
                durability[i] = durability[i] - weight[index];
                flag = true;
                solve(index + 1);
                durability[i] = durability[i] + weight[index];
                durability[index] = durability[index] + weight[i];
            }
            if (flag == false) solve(n);
        }
    }

    @JvmStatic
    fun main(args: Array<String>) = with(System.`in`.bufferedReader()) {
        n = readLine().toInt()
        for (i in 1..n) {
            val temp = readLine().split(" ").map { it.toInt() }.toIntArray()
            durability[i] = temp[0]
            weight[i] = temp[1]
        }

        solve(0)
        println(answer)
    }
}