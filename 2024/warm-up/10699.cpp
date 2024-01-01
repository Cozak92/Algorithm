#include <iostream>
#include <ctime>
#include <string>
#include <stdio.h>

const std::string currentDateTime() {
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Y-%m-%d",&tstruct);
    return buf;
}

int main() {
    std::cout << currentDateTime();
}