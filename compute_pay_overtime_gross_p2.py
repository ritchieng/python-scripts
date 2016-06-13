# Python 2+
# Compute gross pay with overtime parameters
# Author: Ritchie Ng

# Get hourly rate
hourly_rate = raw_input('Hourly rate: ')
# Convert hourly rate to float
hourly_rate = float(hourly_rate)

# Get number of hours
hours = raw_input('Number of hours: ')
# Convert number of hours to float
hours = float(hours)

# Get overtime multiplier
# overtime_m = 1.5 means there is a 50% premium for overtime hours over normal hours
overtime_m = raw_input('Overtime pay multiplier (number of times of normal pay rate): ')
overtime_m = float(overtime_m)

# Get number of hours until overtime takes effect
overtime_ot = raw_input('Number of hours at which overtime takes effect: ')
overtime_ot = float(overtime_ot)

# Creating function to compute gross pay from regular and overtime hours
def computepay(h, r, m, ot):
    # Overtime rate
    overtime_r = r * m

    if h < ot:
        return h * r
    else:
        return (ot * r) + (h - ot) * overtime_r

# Key in parameters to the computepay() function
pay = computepay(hours, hourly_rate, overtime_m, overtime_ot)
print pay
