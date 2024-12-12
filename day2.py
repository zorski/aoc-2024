# read input
data = open('day2-input-sample.txt', 'r').read().split('\n')
results = {
    "safe": 0,
    "unsafe": 0
}

def check_direction(report: list) -> str:
    result = {
        "increasing": 0,
        "decreasing": 0
    }

    for i in range(len(report)-1):
        if report[i+1] > report[i]:
            result["increasing"] += 1
        if report[i+1] < report[i]:
            result["decreasing"] += 1
    
    if result["increasing"] > result["decreasing"]:
        return "increasing"
    else:
        return "decreasing"



for report in data:
    report = [int(x) for x in report.split()]
    direction = check_direction(report)
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
# def check_report(report: list) -> bool:
#     for idx, level in enumerate(report["report"][:-1]):
#         if report["direction"] == "decreasing":
#             if level < report["report"][idx+1]:
                


reports = list()
for idx, report in enumerate(data):
    report = [int(x) for x in report.split()]
    direction = check_direction(report)
    reports.append({"report": report, "bad_levels": [], "result": None, "direction": direction, "problem_dampener": 0})


for idy, report in enumerate(reports):
    report_flag = True
    for idx, value in enumerate(report["report"][:-1]):
        if report["direction"] == "decreasing":
            if report["report"][idx] < report["report"][idx+1]:
                reports[idy]["result"] = False
                reports[idy]["bad_levels"].append(idx)
                reports[idy]["bad_levels"].append(idx+1)
                report_flag = False         
                break
            if report["report"][idx] == report["report"][idx+1]:
                reports[idy]["result"] = False
                reports[idy]["bad_levels"].append(idx)
                reports[idy]["bad_levels"].append(idx+1)
                report_flag = False 
                break
        
        if report["direction"] == "increasing":
            if report["report"][idx] > report["report"][idx+1]:
                reports[idy]["result"] = False
                reports[idy]["bad_levels"].append(idx)
                reports[idy]["bad_levels"].append(idx+1)
                report_flag = False 
                break
            if report["report"][idx] == report["report"][idx+1]:
                reports[idy]["result"] = False
                reports[idy]["bad_levels"].append(idx)
                reports[idy]["bad_levels"].append(idx+1)
                report_flag = False 
                break
        
        if report["direction"] == "flat":
                reports[idy]["result"] = False
                reports[idy]["bad_levels"].append(idx)
                reports[idy]["bad_levels"].append(idx+1)
                report_flag = False 
                break
        
        if abs(report["report"][idx] - report["report"][idx+1]) > 3:
                reports[idy]["result"] = False
                reports[idy]["bad_levels"].append(idx)
                reports[idy]["bad_levels"].append(idx+1)
                report_flag = False 
                break
    if report_flag:
        reports[idy]["result"] = True

results = {
    "all": 1000,
    "s": 0,
    "un": 0
}

results_set = set()

for report in reports:
    report_flag = True

    if report["result"]:
        results_set.add(str(report["report"]))
    else:
        report1 = report["report"].copy()
        report2 = report["report"].copy()
        report1.pop(report["bad_levels"][0])
        report2.pop(report["bad_levels"][1])        

        for idx, value in enumerate(report1[:-1]):
            if report["direction"] == "decreasing":
                if report1[idx] < report1[idx+1]:
                    results["un"] +=1
                    report_flag = False 
                    break
                if report1[idx] == report1[idx+1]:
                    report_flag = False 
                    break
            if report["direction"] == "increasing":
                if report1[idx] > report1[idx+1]:
                    report_flag = False 
                    break
                if report1[idx] == report1[idx+1]:
                    report_flag = False 
                    break
            if report["direction"] == "flat":
                if report1[idx] < report1[idx+1]:
                    report_flag = False 
                    break
            if abs(report1[idx] - report1[idx+1]) > 3:
                report_flag = False 
                break

        if report_flag:
            results_set.add(str(report["report"]))
        
        report_flag = True
        
        for idx, value in enumerate(report2[:-1]):
            if report["direction"] == "decreasing":
                if report2[idx] < report2[idx+1]:
                    report_flag = False 
                    break
                if report2[idx] == report2[idx+1]:
                    report_flag = False 
                    break
            if report["direction"] == "increasing":
                if report2[idx] > report2[idx+1]:
                    report_flag = False 
                    break
                if report2[idx] == report2[idx+1]:
                    report_flag = False 
                    break
            if report["direction"] == "flat":
                if report2[idx] > report2[idx+1]:
                    report_flag = False 
                    break
            if abs(report2[idx] - report2[idx+1]) > 3:
                report_flag = False 
                break

        if report_flag:
            results_set.add(str(report["report"]))


print(len(results_set))




        
            



    



