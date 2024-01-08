def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if target_time is None:
        return None
    for entry in permanence_period:
        if not all(isinstance(time, int) and time >= 0 for time in entry):
            return None
    raise NotImplementedError
