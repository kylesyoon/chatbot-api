from enum import Enum

class Intent(Enum):
    TODAYS_SCHEDULE = 1

    @staticmethod
    def enum_from_string(string):
        if string == 'TodaysSchedule':
            return Intent.TODAYS_SCHEDULE
        else:
            return None
