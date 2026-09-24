def select_meeting_activities(activities):
    activities.sort(key=lambda x: (x[2], x[1], x[0]))

    selected = []
    last_finish = -1

    for activity in activities:
        activity_id, start, finish = activity

        if start >= last_finish:
            selected.append(activity)
            last_finish = finish

    result = []
    result.append("Activity Selection Report")
    result.append("Selected Activities")
    result.append("Activity Start Finish Reason")

    for i, activity in enumerate(selected):
        activity_id, start, finish = activity

        if i == 0:
            reason = "Selected first because it finishes earliest"
        else:
            reason = "Selected because start time is compatible"

        result.append(f"{activity_id} {start} {finish} {reason}")

    result.append(f"Total Selected: {len(selected)}")
    result.append(
        "Justification: Greedy selection by earliest finish time maximizes compatible activities"
    )

    return result