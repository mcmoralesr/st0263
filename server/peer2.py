from concurrent import futures
import grpc
import bittorrent_pb2
import bittorrent_pb2_grpc

class Peer(bittorrent_pb2_grpc.PeerServiceServicer):
    def __init__(self):
        # Almacena los fragmentos de archivos que el peer comparte
        self.files = {}  # Diccionario: archivo -> lista de chunks

    def load_file(self, file_name, chunks):
        """
        Carga un archivo en el peer dividiéndolo en chunks.
        """
        self.files[file_name] = chunks

    def RequestChunk(self, request, context):
        """
        Devuelve el chunk solicitado si existe en este peer.
        """
        file_chunks = self.files.get(request.file_name)
        if not file_chunks or request.chunk_index >= len(file_chunks):
            return bittorrent_pb2.Chunk(chunk_index=request.chunk_index, content=b"")
        return bittorrent_pb2.Chunk(
            chunk_index=request.chunk_index,
            content=file_chunks[request.chunk_index]
        )

def serve():
    """
    Configura y ejecuta el servidor Peer gRPC.
    """
    peer = Peer()

    # Cargar archivo example.txt y dividirlo en chunks
    try:
        with open("example.txt", "rb") as f:
            content = f.read()

        chunk_size = 10  # Tamaño de cada chunk (en bytes)
        chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]

        peer.load_file("example.txt", chunks)
        print(f"Archivo 'example.txt' cargado con {len(chunks)} chunks.")
    except FileNotFoundError:
        print("El archivo 'example.txt' no se encontró. Por favor, créalo en la misma carpeta que este script.")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bittorrent_pb2_grpc.add_PeerServiceServicer_to_server(peer, server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Peer corriendo en puerto 50052...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
