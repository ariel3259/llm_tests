import re

def get_incremental_name(name: str):
    with open("./runs.txt", "r") as f:
        raw_names = f.read()
        f.close()
    name_pattern = re.compile(name + r"-[0-9]{0,12}")
    names: list[str] = name_pattern.findall(raw_names)
    last_index = len(names) - 1
    if last_index >= 0:
        metadatas = names[last_index].split("-")
        id_metadata = metadatas[len(metadatas) - 1]
        id = int(id_metadata) + 1
        name += "-" + str(id)
    else:
        name += "-" + str(1)
    with open("./runs.txt", "w") as f:
            raw_names += name + "\n"
            f.write(raw_names)
            f.close()
    return name