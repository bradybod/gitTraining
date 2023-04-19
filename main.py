import subprocess

def execute_commands(command):
    try:
        process = subprocess.Popen(command.strip().split(), stdout=subprocess.PIPE, stderr = subprocess.PIPE)
        out, err = process.communicate()
        return out.decode("utf-8"), err.decode("utf-8")
    except Exception:
        print("psh: command not found: {}".format(command))

def modify_attendance():
    names = ["John Smith\n", "Yandu Udonta\n", "Wade Wilson\n"]
    attendanceFile = open("Attendance.log", "a")
    attendanceFile.writelines(names)
    attendanceFile.close()

def modify_hello_world():
    helloWorldFile = open("HelloWorld.py", "a")
    helloWorldFile.writeline("print(\"You have reached the end of the file\")")
    helloWorldFile.close()


if __name__ == '__main__':
    execute_commands("git switch -C BranchA")
    execute_commands("touch testing.txt")
    execute_commands("touch file2.txt")
    execute_commands("touch file3.txt")
    modify_attendance()
    modify_hello_world()
    execute_commands("git checkout BranchC")
    execute_commands("touch fileC.cpp")
    execute_commands("git checkout master")
    execute_commands("git merge BranchB")



