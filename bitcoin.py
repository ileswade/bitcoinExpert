import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = (
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(data_string.encode()).hexdigest()

class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.target = '0' * difficulty
        
    def create_genesis_block(self):
        return Block("Genesis Block", "0")
        
    def mine_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        
        print(f"\nMining block containing data: {data}")
        start_time = time.time()
        
        while new_block.hash[:self.difficulty] != self.target:
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
            
            if new_block.nonce % 100000 == 0:
                print(f"Nonce: {new_block.nonce}, Hash: {new_block.hash}")
        
        mining_time = time.time() - start_time
        print(f"\nBlock mined! Time taken: {mining_time:.2f} seconds")
        print(f"Nonce that solved the block: {new_block.nonce}")
        print(f"Block hash: {new_block.hash}")
        
        self.chain.append(new_block)


def main():
    # Create blockchain and mine some blocks
    blockchain = Blockchain(difficulty=4)  # Increase for more challenge
    blockchain.mine_block("First Transaction: Alice sends 5 BTC to Bob")
    blockchain.mine_block("Second Transaction: Bob sends 3 BTC to Charlie")

if __name__ == "__main__":
    main()