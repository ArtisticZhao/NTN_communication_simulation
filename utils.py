from datetime import datetime, timezone, timedelta


def utc_str_to_utc_time(time_string: str) -> datetime:
    time_format = "%d %b %Y %H:%M:%S.%f"

# Parse the time string into a datetime object
    local_time = datetime.strptime(time_string, time_format)

# Assume the local time provided is in a timezone, convert it to UTC
# Here, no timezone information is specified, so assuming it's local time
    utc_time = local_time.replace(tzinfo=timezone(timedelta(hours=0))).astimezone(timezone.utc)
    return utc_time

