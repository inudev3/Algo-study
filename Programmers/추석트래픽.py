import collections


def solution(lines):
    def convert(time):
        hour, min, sec = time.split(":")
        hour = int(hour) * 3600
        min = int(min) * 60
        sec, millisec = list(map(int, sec.split(".")))
        print(hour, min, sec, millisec)
        return (hour + min + sec) * 1000 + millisec

    def getStartTime(time, duration):
        return convert(time) - int(float(duration[:-1]) * 1000) + 1

    start = []
    end = []
    for line in lines:
        time = line.split(" ")
        start.append(getStartTime(time[1], time[2]))
        end.append(convert(time[1]))
    ans = 0
    for i in range(len(lines)):
        cnt = 0
        for j in range(i, len(lines)):
            if end[i] > start[j] - 1000:
                cnt += 1
        ans = max(ans, cnt)
    return ans

collections.deque


