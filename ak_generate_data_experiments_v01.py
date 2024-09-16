import subprocess

# List of commands to run for pendulum
pendulum_commands = [
    "python train.py pendulum --loss_type euler-forw --h 0.1",
    "python train.py pendulum --loss_type euler-symp --h 0.1",
    "python train.py pendulum --loss_type midpoint --h 0.1",
    "python train.py pendulum --loss_type euler-forw --h 0.2",
    "python train.py pendulum --loss_type euler-symp --h 0.2",
    "python train.py pendulum --loss_type midpoint --h 0.2",
    "python train.py pendulum --loss_type euler-forw --h 0.4",
    "python train.py pendulum --loss_type euler-symp --h 0.4",
    "python train.py pendulum --loss_type midpoint --h 0.4",
    "python train.py pendulum --loss_type euler-forw --h 0.05",
    "python train.py pendulum --loss_type euler-symp --h 0.05",
    "python train.py pendulum --loss_type midpoint --h 0.05",
    "python train.py pendulum --loss_type euler-forw --h 0.8",
    "python train.py pendulum --loss_type euler-symp --h 0.8",
    "python train.py pendulum --loss_type midpoint --h 0.8",
]

# List of commands to run for double-pendulum
double_pendulum_commands = [
    "python train.py double-pendulum --loss_type euler-forw --h 0.1",
    "python train.py double-pendulum --loss_type euler-symp --h 0.1",
    "python train.py double-pendulum --loss_type midpoint --h 0.1",
    "python train.py double-pendulum --loss_type euler-forw --h 0.2",
    "python train.py double-pendulum --loss_type euler-symp --h 0.2",
    "python train.py double-pendulum --loss_type midpoint --h 0.2",
    "python train.py double-pendulum --loss_type euler-forw --h 0.4",
    "python train.py double-pendulum --loss_type euler-symp --h 0.4",
    "python train.py double-pendulum --loss_type midpoint --h 0.4",
    "python train.py double-pendulum --loss_type euler-forw --h 0.05",
    "python train.py double-pendulum --loss_type euler-symp --h 0.05",
    "python train.py double-pendulum --loss_type midpoint --h 0.05",
    "python train.py double-pendulum --loss_type euler-forw --h 0.8",
    "python train.py double-pendulum --loss_type euler-symp --h 0.8",
    "python train.py double-pendulum --loss_type midpoint --h 0.8",
]

# List of commands to run for spring
spring_commands = [
    "python train.py spring --loss_type euler-forw --h 0.1",
    "python train.py spring --loss_type euler-symp --h 0.1",
    "python train.py spring --loss_type midpoint --h 0.1",
    "python train.py spring --loss_type euler-forw --h 0.2",
    "python train.py spring --loss_type euler-symp --h 0.2",
    "python train.py spring --loss_type midpoint --h 0.2",
    "python train.py spring --loss_type euler-forw --h 0.4",
    "python train.py spring --loss_type euler-symp --h 0.4",
    "python train.py spring --loss_type midpoint --h 0.4",
    "python train.py spring --loss_type euler-forw --h 0.05",
    "python train.py spring --loss_type euler-symp --h 0.05",
    "python train.py spring --loss_type midpoint --h 0.05",
    "python train.py spring --loss_type euler-forw --h 0.8",
    "python train.py spring --loss_type euler-symp --h 0.8",
    "python train.py spring --loss_type midpoint --h 0.8",
]

# Combine all commands
all_commands = pendulum_commands + double_pendulum_commands + spring_commands

# Execute each command
for cmd in all_commands:
    print(f"Running command: {cmd}")
    process = subprocess.run(cmd, shell=True)
    # Check if the command was successful
    if process.returncode != 0:
        print(f"Command failed: {cmd}")
    else:
        print(f"Command succeeded: {cmd}")
