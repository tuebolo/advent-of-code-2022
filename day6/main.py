def get_marker(datastream, stop):
    packet = []
    for idx, marker in enumerate(datastream):
        packet.append(marker)
        if len(set(packet)) < len(packet):
            packet = packet[1:]
        if len(packet) == stop:
            return idx+1


if __name__ == "__main__":
    with open('input.txt', "r") as f:
        datastream = f.read()

    print(get_marker(datastream, 14))
