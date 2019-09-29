import requests, sys, re


def howUse():
        print(f" _                     _\n"                         
                "| |                   | |\n"                        
                "| |__   _____      __ | |_ ___    _   _ ___  ___\n" 
                "| '_ \ / _ \ \ /\ / / | __/ _ \  | | | / __|/ _ \\\n"
                "| | | | (_) \ V  V /  | || (_) | | |_| \__ \  __/\n"
                "|_| |_|\___/ \_/\_/    \__\___/   \__,_|___/\___|\n"
                "                                                 \n"
                f"Ex: python {sys.argv[0]} <url?param=> <line,line> <payload>\n"
                "Type -s at the end to see the lines\n"
                f"Ex: python {sys.argv[0]} <url?param=> -s")


def detectLine(url, back):
        headers = {'User-Agent': "Googlebot"}

        code = []
        payload = sys.argv[3]

        r = requests.get(f"{url}{payload}", headers=headers)
        lines = r.text.replace("\t", "")
        liners = lines.split("\n")
        for line in liners:
                code.append(line)

        if back == 1:
                for i in range(0, len(code)):
                        print(f"{i} || {code[i]}")
        if back == 0:
                return (code)


if len(sys.argv) < 3 and sys.argv[-1] != "-s":
        howUse()
        exit()
elif sys.argv[-1] == "-s":
        detectLine(sys.argv[1], 1)
        exit()

codeLines = detectLine(sys.argv[1], 0)
numberLines = []
payload = sys.argv[3]

for i in sys.argv[2].split(","):
        numberLines.append(i)

print(f"||URL||> {sys.argv[1]}{sys.argv[3]}")

for nl in numberLines:
        for cl in range(0, len(codeLines)):
                if int(nl) == cl:
                        print(f"{codeLines[cl]}")

