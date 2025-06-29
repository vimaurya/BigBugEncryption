# Modular arithmetic based encryption

A custom cryptographic algorithm designed for fun and educational purposes, using time-inspired keys and stateful substitution.

## Features

- **144 unique key combinations** based on modular arithmetic
- **Dual-layer encryption** with hour (`h`) and minute (`m`) keys
- **Stateful toggles** (`hosc`/`mosc`) that flip during processing
- **Special handling** for non-alphabetic characters and y/z swaps
- **Simple CLI interface** for encryption/decryption

## How It Works

### Key Generation
1. Accepts hour (`h`) and minute (`m`) values as keys
2. Normalizes keys using `fix_key()`:
   - `h = h % 12` (converts to 12-hour format)
   - `m = m // 5` (groups minutes into 5-minute blocks)

### Encryption/Decryption
- Characters are divided into:
  - **Hour group (a-l)**: Modified by `h` key with `hosc` toggle
  - **Minute group (m-x)**: Modified by `m` key with `mosc` toggle
  - **Special group (y,z)**: Always swapped with each other
- Toggles flip after processing their respective character groups

## Usage

1. Clone the repository
2. Run the script:
   ```bash
   python cipher.py
