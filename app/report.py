def generate_report(result):

    report = []

    report.append(
        "CONFIGURATION COMPARISON REPORT"
    )

    report.append("\nADDED")

    report.append(
        str(result["added"])
    )

    report.append("\nREMOVED")

    report.append(
        str(result["removed"])
    )

    report.append("\nMODIFIED")

    report.append(
        str(result["modified"])
    )

    return "\n".join(report)