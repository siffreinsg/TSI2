def deg2dms(deg_angle):
    degres = int(deg_angle)
    minutes = int((deg_angle - degres) * 60)
    seconds = ((deg_angle - degres) * 60 - minutes) * 60

    return (degres, minutes, seconds)


def dms2deg(dms_angle):
    return dms_angle[0] + (dms_angle[1]/60) + (dms_angle[2]/3600)


test_values = [
    # (value in deg, value in dms)
    (123.789657, (123, 47, 22.7652)),
    (0, (0, 0, 0)),
    (-123.789657, (-123, -47, -22.7652))
]

for test_value in test_values:
    calculated_dms = deg2dms(test_value[0])
    calculated_deg = dms2deg(test_value[1])

    print(calculated_deg, calculated_dms)
