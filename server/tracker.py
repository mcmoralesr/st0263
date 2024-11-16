from concurrent import futures
import grpc
import bittorrent_pb2
import bittorrent_pb2_grpc

class Tracker(bittorrent_pb2_grpc.TrackerServiceServicer):
    def __init__(self):
        self.peers = {}  # Registro de peers: {peer_id: {address, files}}

    def RegisterPeer(self, request, context):
        self.peers[request.peer_id] = {
            "address": request.address,
            "files": list(request.files)
        }
        return bittorrent_pb2.Status(message="Peer registrado exitosamente")

    def GetPeers(self, request, context):
        peer_list = [
            bittorrent_pb2.PeerInfo(
                peer_id=peer_id,
                address=info["address"],
                files=info["files"]
            )
            for peer_id, info in self.peers.items()
            if request.file_name in info["files"]
        ]
        return bittorrent_pb2.PeerList(peers=peer_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bittorrent_pb2_grpc.add_TrackerServiceServicer_to_server(Tracker(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Tracker corriendo en puerto 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

