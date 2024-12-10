# read input
data = open('day2-input-sample.txt', 'r').read().split('\n')
results = {
    "safe": 0,
    "unsafe": 0
}

def check_direction(report: list) -> str:
    if report[0] > report[1]:
        return "decreasing"
    if report[0] < report[1]:
        return "increasing"
    if report[0] == report[1]:
        return "flat"

for report in data:
    report = [int(x) for x in report.split()]
    direction = check_direction(report)
    print(direction)
    for idx, value in enumerate(report[:-1]):
        if direction == "decreasing":
            if report[idx] < report[idx+1]:
                results["unsafe"] +=1
                break
            if report[idx] == report[idx+1]:
                results["unsafe"] += 1
                break
        if direction == "increasing":
            if report[idx] > report[idx+1]:
                results["unsafe"] +=1
                break
            if report[idx] == report[idx+1]:
                results["unsafe"] += 1
                break
        if direction == "flat":
            results["unsafe"] += 1
            break
        if abs(report[idx] - report[idx+1]) > 3:
            results["unsafe"] += 1
            break
    results["safe"] += 1

print(results["safe"] - results["unsafe"])

# PART 2
results2 = {
    "safe": 0,
    "unsafe": 0
}


reports = list()
for idx, report in enumerate(data):
    report = [int(x) for x in report.split()]
    direction = check_direction(report)
    reports.append({"report": report, "alternatives": [], "result": None, "direction": direction, "problem_dampener": 0})


for idy,report in enumerate(reports):
    for idx, value in enumerate(report["report"][:-1]):
        if report["direction"] == "decreasing":
            if report[idx] < report[idx+1]:
                if report["problem_dampener"] == 0:
                    reports[idy]["problem_dampener"] += 1
                    report_alt_1 = report["report"].copy()
                    report_alt_2 = report["report"].copy()
                    reports[idy]["alternatives"].append(report_alt_1.pop(idx))
                    reports[idy]["alternatives"].append(report_alt_1.pop(idx+1))
                else: 
                    reports[idy]["result"] = False
                    break
                
            



    



