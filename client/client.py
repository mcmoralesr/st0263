import grpc
import bittorrent_pb2
import bittorrent_pb2_grpc
import argparse

def main(tracker_ip, tracker_port, peer_ip, peer_port):
    # Construir la dirección del tracker
    tracker_address = f"{tracker_ip}:{tracker_port}"
    peer_address = f"{peer_ip}:{peer_port}"

    # Conectar al servidor tracker
    with grpc.insecure_channel(tracker_address) as channel:
        tracker_stub = bittorrent_pb2_grpc.TrackerServiceStub(channel)

        # Registrar un peer en el tracker
        print("Registrando un peer...")
        try:
            response = tracker_stub.RegisterPeer(
                bittorrent_pb2.PeerInfo(
                    peer_id="peer1",           # ID del peer
                    address=peer_address,      # Dirección del peer
                    files=["example.txt"]      # Archivos que comparte
                )
            )
            print(response.message)
        except grpc.RpcError as e:
            print(f"Error registrando el peer: {e.details()} (código: {e.code()})")

        # Solicitar lista de peers que comparten un archivo
        print("Obteniendo lista de peers...")
        try:
            peer_list = tracker_stub.GetPeers(
                bittorrent_pb2.FileRequest(file_name="example.txt")
            )
            if peer_list.peers:
                for peer in peer_list.peers:
                    print(f"Peer encontrado: {peer.peer_id} - Dirección: {peer.address}")
            else:
                print("No se encontraron peers compartiendo el archivo.")
        except grpc.RpcError as e:
            print(f"Error obteniendo la lista de peers: {e.details()} (código: {e.code()})")

    # Solicitar chunk desde un peer
    request_chunk_from_peer(peer_address)

def request_chunk_from_peer(peer_address):
    """
    Solicita un fragmento específico de un archivo desde un peer.
    """
    with grpc.insecure_channel(peer_address) as channel:
        peer_stub = bittorrent_pb2_grpc.PeerServiceStub(channel)

        # Solicita el fragmento 0 del archivo "example.txt"
        print("Solicitando chunk del peer...")
        try:
            response = peer_stub.RequestChunk(
                bittorrent_pb2.ChunkRequest(
                    file_name="example.txt",
                    chunk_index=0
                )
            )
            print(f"Chunk recibido (index {response.chunk_index}): {response.content.decode()}")
        except grpc.RpcError as e:
            print(f"Error solicitando el chunk: {e.details()} (código: {e.code()})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente BitTorrent simple")
    parser.add_argument("--tracker_ip", type=str, required=True, help="IP del tracker")
    parser.add_argument("--tracker_port", type=int, required=True, help="Puerto del tracker")
    parser.add_argument("--peer_ip", type=str, required=True, help="IP del peer")
    parser.add_argument("--peer_port", type=int, required=True, help="Puerto del peer")

    args = parser.parse_args()
    main(args.tracker_ip, args.tracker_port, args.peer_ip, args.peer_port)
