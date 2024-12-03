
# Document Verification with Blockchain

This project implements a document verification system using blockchain technology. It leverages cryptographic techniques to ensure data integrity and authenticity, providing a secure and transparent framework for document validation.

## Features
- Blockchain-based verification system.
- Secure storage of documents with cryptographic signatures.
- Automated validation using hashing and digital signatures.
- User-friendly interface for uploading and verifying documents.

## Project Structure
```
doc-verification-with-blockchain-main/
├── .gitignore               # Git ignore file
├── Blockchain/              # Main application directory
│   ├── Blockchain/          # Core blockchain module
│   ├── HomePage/            # Frontend application files
│   ├── Result.txt           # Stores blockchain output results
│   ├── block.txt            # Blockchain ledger data
│   ├── db.sqlite3           # SQLite database for application data
│   ├── hash.txt             # Hash of the latest blockchain block
│   ├── key.py               # Key generation and management scripts
│   ├── manage.py            # Django management script
│   ├── media/               # Media directory for uploaded documents
│   ├── message.txt          # Sample blockchain messages
│   ├── privatekey.key       # Private key for cryptographic operations
│   ├── publickey.key        # Public key for cryptographic operations
│   ├── sign_hash.txt        # Signed hash file
│   ├── signature_file       # Digital signature file
│   ├── signature_file2      # Secondary signature file
├── main.py                  # Entry point for the application
```

## Requirements
- Python 3.x
- Django
- SQLite3

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd doc-verification-with-blockchain-main
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   python Blockchain/manage.py runserver
   ```

## Usage
1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Upload documents for verification.
3. View results to confirm document authenticity.

## Security
This project implements blockchain technology to ensure:
- Tamper-proof document storage.
- Verified digital signatures.
- Secure key management.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contribution
Contributions are welcome! Please fork the repository and create a pull request.

## Acknowledgements
Special thanks to the developers and the open-source community for their contributions to this project.
