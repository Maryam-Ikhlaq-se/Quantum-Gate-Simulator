import math

# --- Qubit ---
def make_qubit(alpha, beta):
    assert abs(pow(alpha,2) + pow(beta,2) - 1.0) < 1e-9, "Invalid qubit"
    return [alpha, beta]

def state_zero():
    return make_qubit(1.0, 0.0)  # pure 0 state

def state_one():
    return make_qubit(0.0, 1.0)  # pure 1 state

# --- Hadamard Gate ---
def hadamard(qubit):
    alpha, beta = qubit
    new_alpha = (1/math.sqrt(2)) * (alpha + beta)
    new_beta  = (1/math.sqrt(2)) * (alpha - beta)
    return make_qubit(new_alpha, new_beta)

# --- Run ---
print("=== Quantum Gate Simulator ===\n")

q = state_zero()
print(f"Before H gate: {q}")

q = hadamard(q)
print(f"After H gate:  {q}")

q = hadamard(q)
print(f"After H again: {q}")

print("\n--- State One Test ---")
q = state_one()
print(f"Before H gate: {q}")

q = hadamard(q)
print(f"After H gate:  {q}")

q = hadamard(q)
print(f"After H again: {q}")