import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Create a hash by combining block attributes
        block_string = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Genesis block, the first block in the blockchain
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Check the validity of the blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the current block points to the correct previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Example usage
zord_blockchain = Blockchain()

# Adding new blocks to the ZORD blockchain
zord_blockchain.add_block(Block(1, "", time.time(), "First Block Data"))
zord_blockchain.add_block(Block(2, "", time.time(), "Second Block Data"))

# Printing the blockchain
for block in zord_blockchain.chain:
    print(f"Block {block.index} [")
    print(f"   Timestamp: {block.timestamp}")
    print(f"   Data: {block.data}")
    print(f"   Previous Hash: {block.previous_hash}")
    print(f"   Hash: {block.hash}")
    print("]")

# Check blockchain validity
print("\nIs Blockchain Valid?", zord_blockchain.is_chain_valid())
