import subprocess
import sys

# Check if the script received the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python3 run_commands.py <input_file>")
    sys.exit(1)

# Get the input file from the command-line arguments
input_file = sys.argv[1]

# Define the command to run main.py
command1 = ["python3", "main.py", input_file]

# Open the output file
with open("test_llvm/output.ll", "w") as output_file:
    # Run the first command and redirect its output to the file
    subprocess.run(command1, stdout=output_file, text = True)

# Define the second command
command2 = ["lli", "-opaque-pointers", "test_llvm/output.ll"]

# Run the second command
subprocess.run(command2, check=True)