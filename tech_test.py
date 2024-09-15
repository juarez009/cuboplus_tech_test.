import hashlib
import time

def calculate_hash(block, nonce):
    """Calculates the hash of a block with a specific nonce."""
    block_str = str(block) + str(nonce)
    return hashlib.sha256(block_str.encode()).hexdigest()

def valid_hash(hash, difficulty):
    """Checks if the hash is valid according to the difficulty level (number of leading zeros)."""
    return hash.startswith('0' * difficulty)

def simulate_pow(block, difficulty):
    """Simulates the calculation of multiple hashes until one meets the target."""
    nonce = 0
    start_time = time.time()
    
    # Loop to calculate multiple hashes until a valid one is found
    while True:
        hash_result = calculate_hash(block, nonce)
        if valid_hash(hash_result, difficulty):
            end_time = time.time()
            time_taken = end_time - start_time
            return nonce, hash_result, time_taken
        nonce += 1

def run_simulation(block, difficulties):
    """Displays the time it takes to find a valid hash at different difficulty levels."""
    for difficulty in difficulties:
        print(f"\nSimulating for difficulty {difficulty}:")
        nonce, valid_hash_result, time_taken = simulate_pow(block, difficulty)
        print(f"Valid hash found: {valid_hash_result}")
        print(f"Nonce: {nonce}")
        print(f"Time taken: {time_taken:.4f} seconds")

# Set the test block and difficulty levels
block = input("Put the block to start the simulation:  ")

# List of difficulties (number of leading zeros required in the hash)
difficulties = [2, 3, 4]

# Run the simulation for different difficulty levels
run_simulation(block, difficulties)
