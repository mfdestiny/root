import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = []
    pattern = re.split(r' to ',s)
    if pattern[0] == s:
        raise ValueError("Incorrect format")
    for match in pattern:
        p1 = re.compile(r"\d+|(\d\d)")
        m = p1.finditer(match)
        for e in m:
            time.append(e.group(0))
    tz1 = re.compile("AM")
    tz2 = re.compile("PM")
    t1 = tz1.finditer(s)
    t2 = tz2.finditer(s)
    if re.search("AM",s):
        for t in t1:
            if s[t.start()-1] == " ":
                time.append(t.start())
            else:
                raise ValueError("Incorrect format")
    else:
        raise ValueError("Incorrect format")
    if re.search("PM",s):
        for t in t2:
            if s[t.start()-1] == " ":
                time.append(t.start())
            else:
                raise ValueError("Incorrect format")
    else:
        raise ValueErrror("Incorrect format")

    if len(time) == 6:
        begin = int(time[0])
        end = int(time[2])
        if int(time[1]) > 59 or int(time[3]) > 59 or int(time[0]) > 12 or int(time[2]) > 12:
            raise ValueError("Invalid time")
        if time[4] < time[5]: # 12AM to 12PM = 0:24
            conv1 = int(time[0])
            if conv1 == 12:
                conv1 = 0
            if int(time[2]) != 12:
                conv2 = int(time[2]) + 12
            else:
                conv2 = int(time[2])
            return (f"{conv1:02}:{time[1]} to {conv2}:{time[3]}")
        else: #12PM to 12AM 24:0
            if int(time[0]) != 12:
                conv1 = int(time[0]) + 12
            else:
                conv1 = int(time[0])
            conv2 = int(time[2])
            if conv2 == 12:
                conv2 = 0
        return (f"{conv1}:{time[1]} to {conv2:02}:{time[3]}")
    elif len(time) == 4:
        begin = int(time[0])
        end = int(time[1])
        if begin > 12 or end > 12:
            raise ValueError("Invalid time")
        if time[2] < time[3]: #12AM to 12PM 0:24
            conv1 = begin
            if conv1 == 12:
                conv1 = 0
            if end != 12:
                conv2 = end + 12
            else:
                conv2 = end
            return (f"{conv1:02}:00 to {conv2}:00")
        else: # 12PM to 12AM 24:0
            if begin != 12:
                conv1 = begin + 12
            else:
                conv1 = begin
            conv2 = end
            if conv2 == 12:
                conv2 = 0
        return (f"{conv1}:00 to {conv2:02}:00")
    else:
        raise ValueError("error")



if __name__ == "__main__":
    main()
