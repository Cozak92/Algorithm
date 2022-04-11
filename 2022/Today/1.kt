package `2022`.Today

import java.util.*

val stack = Stack<Char>()
val answer = Stack<String>()
fun solve(path: String) {
    var totaltime = 0
    var curtime = 0
    var distance = 0
    var direction = ""
    for (p in path) {
        totaltime++
        if (stack.peek() == p || stack.empty()) {
            // 현재시간 늘어남
            curtime++
        } else if (stack.peek() != p) {
            if (stack.peek() == 'E') {
                direction = if (p == 'S') {
                    "right"
                } else {
                    "reft"
                }
            } else if (stack.peek() == 'S') {
                direction = if (p == 'E') {
                    "right"
                } else {
                    "reft"
                }
            } else if (stack.peek() == 'W') {
                direction = if (p == 'N') {
                    "right"
                } else {
                    "reft"
                }
            } else if (stack.peek() == 'N') {
                direction = if (p == 'E') {
                    "right"
                } else {
                    "reft"
                }
            }
            var time = 0
            if(curtime >= 6){
                 time = totaltime - 5
            } else {
                time = totaltime-curtime
            }

            answer.push("Time {$time}: Go straight {$time}M and turn {$direction}")

        }
    }

    print(answer)
}


fun main() {
    solve("EEESEEEEEENNNN")
}