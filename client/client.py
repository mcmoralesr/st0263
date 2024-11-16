import grpc
import bittorrent_pb2
import bittorrent_pb2_grpc

def main():
    # Conectar al servidor tracker (puerto 50051)
    with grpc.insecure_channel('localhost:50051') as channel:
        tracker_stub = bittorrent_pb2_grpc.TrackerServiceStub(channel)
        
        # Registrar un peer en el tracker
        print("Registrando un peer...")
        try:
            response = tracker_stub.RegisterPeer(
                bittorrent_pb2.PeerInfo(
                    peer_id="peer1",           # ID del peer
                    address="localhost:50052", # Dirección del peer
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

if __name__ == "__main__":
    main()

