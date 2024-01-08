def is_valid_entry(entry):
    return all(isinstance(time, int) and time >= 0 for time in entry)


def count_students_in_target_time(permanence_period, target_time):
    student_count = 0

    for entry in permanence_period:
        if entry[0] <= target_time <= entry[1]:
            student_count += 1

    return student_count


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if any(not is_valid_entry(entry) for entry in permanence_period):
        return None

    return count_students_in_target_time(permanence_period, target_time)
