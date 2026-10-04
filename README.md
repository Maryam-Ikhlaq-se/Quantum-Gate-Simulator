# Quantum Gate Simulator

## Project 2: Quantum Gate Simulator

### What This Project Does
This project applies a Hadamard Gate to a qubit and shows how a definite 
state transforms into superposition and back again.
---

### Background Math From Scratch

#### What is a Qubit?
A qubit is represented as two numbers in a list:

qubit = [alpha, beta]

These numbers are called amplitudes, not probabilities.
To get probability, square the amplitude. This is called the Born Rule:

P(0) = alpha²
P(1) = beta²
alpha² + beta² = 1.0 ← always


#### What is a Matrix?
A matrix is numbers arranged in rows and columns:

[ 1 2 ]
[ 3 4 ]

This is a 2x2 matrix, 2 rows and 2 columns.

#### What is Matrix Multiplication?
When we multiply a 2x2 matrix with a qubit:

[ a b ] [ x ] [ ax + by ]
[ c d ] × [ y ] = [ cx + dy ]

Each row of matrix multiplies with the qubit, element by element, then adds.

#### What is the Hadamard Gate?
A quantum gate is a matrix that transforms a qubit.
The Hadamard Gate is defined as:

H = 1/√2 × [ 1 1 ]
[ 1 -1 ]

Why 1/√2?
Because output must also be a valid qubit, alpha² + beta² = 1.0.
Without 1/√2:

1² + 1² = 2 ≠ 1.0  (wrong)

With 1/√2 = 0.707:

0.707² + 0.707² = 0.5 + 0.5 = 1.0 (correct)

Why is there a -1 in the matrix?
Because applying H twice must return the original state.
The -1 ensures this mathematically:

[1.0, 0.0] → H → [0.707, 0.707] → H → [1.0, 0.0]

Without -1, applying H twice would give an invalid qubit.

#### What is Phase?
When H is applied to state one [0.0, 1.0]:

After H: [0.707, -0.707]

The negative sign is called phase.
It does not affect probability:

(-0.707)² = 0.5 = 50% ← same as 0.707²

But phase matters in quantum interference, covered in Project 3.

---

### States Used

**State Zero [1.0, 0.0]**

P(0) = 1.0² = 100%
P(1) = 0.0² = 0%

Definite state, no superposition.

**State One [0.0, 1.0]**

P(0) = 0.0² = 0%
P(1) = 1.0² = 100%

Definite state, no superposition.

**After Hadamard [0.707, 0.707]**

P(0) = 0.707² = 50%
P(1) = 0.707² = 50%

Equal superposition, both possibilities exist.

---

### Real World Applications of Hadamard Superposition

The Hadamard Gate is not just a mathematical concept. It is the
foundation of almost every quantum computing application that exists today.

**Quantum Search (Grover's Algorithm)**
In a classical computer, searching through 1 million items requires
checking them one by one. A quantum computer applies the Hadamard Gate
to put all 1 million possibilities into superposition at once, then
finds the answer in roughly 1000 steps instead of 1 million.

**Quantum Cryptography**
When two people want to share a secret key securely, Hadamard superposition
is used to generate truly random keys. Classical computers generate
pseudo random numbers, meaning there is a pattern hidden somewhere.
Quantum superposition produces genuine randomness because the value does
not exist until measured.

**Quantum Machine Learning**
Training an AI model classically means processing data point by point.
Hadamard Gate puts all data points into superposition simultaneously,
allowing a quantum computer to process entire datasets in parallel.
Companies like Google and IBM are currently researching this.

**Breaking Encryption (Shor's Algorithm)**
Current internet encryption relies on the fact that factoring large numbers
takes classical computers thousands of years. Shor's Algorithm uses
Hadamard superposition to explore all possible factors simultaneously,
potentially breaking current encryption in minutes. This is why governments
are investing heavily in quantum safe encryption right now.

**Quantum Simulation**
Simulating how molecules behave is impossible for classical computers
because the number of quantum states grows exponentially. Hadamard
superposition allows a quantum computer to naturally represent all
those states at once. This directly impacts drug discovery and
materials science.

---

### Code Explanation

**`make_qubit(alpha, beta)`**
Validates and returns a qubit as a list.
Uses assert with 1e-9 tolerance instead of ==
because decimal numbers in computers are never perfectly exact.

**`state_zero()`**
Returns [1.0, 0.0], pure 0 state.

**`state_one()`**
Returns [0.0, 1.0], pure 1 state.

**`hadamard(qubit)`**
Applies Hadamard Gate using matrix multiplication:

new_alpha = 0.707 × (alpha + beta) ← first row of H matrix
new_beta = 0.707 × (alpha - beta) ← second row, minus because of -1


### How to Run
```bash
python quantum_gate.py
```

### Output Explained

Before H gate: [1.0, 0.0] ← pure 0 state
After H gate: [0.707, 0.707] ← superposition
After H again: [1.0, 0.0] ← back to original, H is its own reverse

Before H gate: [0.0, 1.0] ← pure 1 state
After H gate: [0.707, -0.707] ← superposition with phase
After H again: [0.0, 1.0] ← back to original

### Project Setup Explained

**Why Virtual Environment?**
Every project gets its own isolated room.
If we install packages globally, different projects can conflict with each other.
For example, Project 1 might need pytest 9.1 and Project 3 might need pytest 9.5.
Virtual environment keeps each project's packages separate and clean.
Command used:

python -m venv .venv
.venv\Scripts\activate


**Why pytest?**
pytest checks if our code is working correctly.
We write a test that says "this function should return this value"
and pytest confirms it does. It catches bugs before they become problems.

**Why black?**
black is an automatic code formatter.
When we save a file, black fixes indentation, spacing, and style automatically.
We focus on logic, black handles the looks.

**Why pylint?**
pylint is a code grammar checker.
If we use a variable that was never defined, or make a logical mistake,
pylint shows a warning in VS Code in real time.
It is like spell check but for Python code.

**Why pytest, black and pylint together?**

pytest → does code work correctly?
black → does code look clean?
pylint → does code have any mistakes?

Together they make sure code is correct, clean and error free.

### My Learnings
- A quantum gate is just a matrix
- Matrix multiplication transforms a qubit
- Hadamard Gate creates equal superposition from a definite state
- 1/√2 ensures output remains a valid qubit
- The -1 in the matrix ensures H applied twice returns original state
- Negative amplitude is called phase and does not affect probability
- Computers cannot store decimals perfectly, always use tolerance not ==