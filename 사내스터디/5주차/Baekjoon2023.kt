package Baekjoon.사내스터디.`5주차`

import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader


object Baekjoon2023 {
    var n = 0
    var sb: StringBuilder? = null
    var alwaysSosu = arrayOf("1", "3", "7", "9")

    @Throws(NumberFormatException::class, IOException::class)
    @JvmStatic
    fun main(args: Array<String>) {
        val br = BufferedReader(InputStreamReader(System.`in`))
        n = Integer.valueOf(br.readLine())
        sb = StringBuilder()

        // 한 자리의 소수는 고정되어이쓰므로, 이거부터 시작하기
        val startSosu = arrayOf("2", "3", "5", "7")
        for (i in startSosu.indices) {
            backTracking(startSosu[i], 1)
        }
        print(sb.toString())
    }

    // 백트래킹
    // 자리 수 하나씩 증가할 때 마다, 해당 함수 재귀호출
    fun backTracking(sosu: String, len: Int) {
        if (len >= n) {
            sb!!.append(sosu).append("\n")
            return
        }
        for (i in alwaysSosu.indices) {
            val nextSosu = sosu + alwaysSosu[i]
            val nextSosuNumber = Integer.valueOf(nextSosu)
            if (isSosu(nextSosuNumber)) {
                backTracking(nextSosu, len + 1)
            }
        }
    }

    // 해당 수가 소수인지 체크하기
    // 에라토스테네스의 체 이용
    fun isSosu(num: Int): Boolean {
        val sqrt = Math.sqrt(num.toDouble()).toInt()
        for (i in 2..sqrt) {
            if (num % i == 0) {
                return false
            }
        }
        return true
    }
}