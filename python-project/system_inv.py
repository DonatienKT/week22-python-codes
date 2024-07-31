import platform
import psutil
import subprocess
import sys

def get_system_info():
    # Get OS information
    os_name = platform.system()
    os_version = platform.release()

    # Get CPU information
    cpu_count = psutil.cpu_count()

    # Get memory information
    memory = psutil.virtual_memory()
    memory_total = round(memory.total / (1024.0 ** 3), 2)  # Convert bytes to GB

    # Get Python version
    python_version = sys.version.split(" ")[0]

    return os_name, os_version, cpu_count, memory_total, python_version

def main():
    os_name, os_version, cpu_count, memory_total, python_version = get_system_info()

    print("System Information:")
    print(f"Operating System: {os_name} {os_version}")
    print(f"CPU Count: {cpu_count}")
    print(f"Memory Size: {memory_total} GB")
    print(f"Python Version: {python_version}")

if __name__ == "__main__":
    main()