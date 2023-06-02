def make_readable(time_in_seconds):

    human_readable_hr = time_in_seconds// 3600
    human_readable_min = (time_in_seconds - human_readable_hr * 3600) // 60
    human_readable_sec = time_in_seconds - (human_readable_hr * 3600) -  (human_readable_min * 60)

    return f"{human_readable_hr:0>2d}:{human_readable_min:0>2d}:{human_readable_sec:0>2d}"

print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))