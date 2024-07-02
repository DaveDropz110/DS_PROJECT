class ConsistentHash:
    def __init__(self, num_slots=512, num_virtual_servers=9):
        # Initialize the hash ring
        self.num_slots = num_slots
        self.num_virtual_servers = num_virtual_servers
        self.hash_ring = {}

    def add_server(self, server_id):
        # Add a server to the hash ring
        for i in range(self.num_virtual_servers):
            slot = self._hash_function(server_id, i) % self.num_slots
            self.hash_ring[slot] = server_id

    def remove_server(self, server_id):
        # Remove a server from the hash ring
        self.hash_ring = {k: v for k, v in self.hash_ring.items() if v != server_id}

    def get_server(self, request_id):
        # Get the server for a request
        if not self.hash_ring:
            return None
        slot = self._request_hash_function(request_id) % self.num_slots
        for i in range(self.num_slots):
            server = self.hash_ring.get((slot + i) % self.num_slots)
            if server:
                return server

    def _hash_function(self, i, j):
        # Hash function for server
        return i**2 + j**2 + 2*j + 25

    def _request_hash_function(self, i):
        # Hash function for request
        return i**2 + 2*i + 17
