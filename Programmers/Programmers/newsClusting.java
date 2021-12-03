package Programmers.Programmers;

import java.util.ArrayList;
import java.util.Locale;

public class newsClusting {
    public int solution(String str1, String str2) {
        ArrayList<String> sortedStr1 = new ArrayList<>();
        ArrayList<String> sortedStr2 = new ArrayList<>();
        ArrayList<String> intersection = new ArrayList<>();
        ArrayList<String> union = new ArrayList<>();
        int answer = 0;

        sortedStr1 = sortString(str1.toLowerCase(), sortedStr1);
        sortedStr2 = sortString(str2, sortedStr2);

        for (String part : sortedStr1) {
            if (sortedStr2.remove(part)) {
                intersection.add(part);
            }

            union.add(part);
        }

        union.addAll(sortedStr2);

        if (union.isEmpty()) {
            answer = 1;
        } else {
            answer = (int) (intersection.size() / union.size());
        }


        return answer * 65536;
    }

    public ArrayList<String> sortString(String str, ArrayList<String> sortedStr) {
        for (int i = 0; i < str.length(); i++) {
            char a = str.charAt(i);
            char b = str.charAt(i);

            if ('a' <= a && a <= 'z' && 'a' <= b && b <= 'z') {
                sortedStr.add(a + "" + b);
            }
        }

        return sortedStr;
    }
}
