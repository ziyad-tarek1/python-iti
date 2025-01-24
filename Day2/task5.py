
# 5-Write a script that checks the available disk space:
# 	GET DISK FROM USER
# 	If the disk space is less than 10%, print "Warning: Low disk space!".

# 	If the disk space is between 10% and 20%, print "Warning: Disk space is getting low.".

# 	Otherwise, print "Disk space is sufficient.".

# Simulated disk data
disks = {
    '/dev/vda1': {'total': 100, 'used': 20},
    '/dev/vdb1': {'total': 200, 'used': 180},
    '/dev/vdc1': {'total': 150, 'used': 120},
    '/dev/vdd1': {'total': 250, 'used': 200},
}

# Display available disks
print("Available disks on the host are:")
for disk in disks.keys():
    print(disk)

# Get user input
selected_disk = input("Choose which disk you want to check: ")

# Check if the selected disk exists
if selected_disk in disks:
    # Calculate available disk space percentage
    total = disks[selected_disk]['total']
    used = disks[selected_disk]['used']
    available_percentage = ((total - used) / total) * 100

    # Display the calculated free space percentage
    print(f"Disk {selected_disk} has {available_percentage:.2f}% free space.")

    # Provide warnings based on free space
    if available_percentage < 10:
        print("Warning: Low disk space!")
    elif 10 <= available_percentage < 20:
        print("Warning: Disk space is getting low.")
    else:
        print("Disk space is sufficient.")
else:
    print("Error: The selected disk does not exist.")
