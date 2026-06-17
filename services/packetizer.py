JPEG_PATH = TEMPORARY_PATH_NAME
SIZE = 512

def packetize_text(file_path, packet_size):
    with open(file_path, 'rb') as f:
        text_data = f.read()

    # must be a byte array
    text_byte = bytearray(text_data, "utf-8")


def packetize_jpeg(file_path, packet_size=512):
    with open(file_path, 'rb') as f:
        jpeg_data = f.read()

    packets = []
    total_size = len(jpeg_data)
    
    for i in range(0, total_size, packet_size):
        packet_payload = jpeg_data[i:i + packet_size]
        
        header = {
            'packet_num':len(packets),
            'payload_size': len(packet_payload),
            'is_last': (i + packet_size) >= total_size
        }
        
        packets.append({
            'header': header,
            'payload': packet_payload
        })

    print(f"Packetized {total_size} bytes into {len(packets)} packets.")
    return packets

packetize_jpeg(JPEG_PATH, packet_size = SIZE)
