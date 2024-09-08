# BeyzInfectify

## Introduction

Welcome to the BeyzInfectify! This project is designed to help you detect malicious software by scanning files and comparing their hash values against a known malware database. The primary goal is to create a tool that identifies malware using file hashes, making the detection process efficient and reliable.



### Features
- Hash-Based Detection: Utilizes SHA-256 hashing to identify potentially malicious files.
- Database Integration: Incorporates a malware hash database for accurate detection.
- Directory Scanning: Recursively scans directories to analyze all contained files.
- Logging: Records scan results in a log file for easy review.



### Installation
Follow these steps to set up the BeyzInfectify on your local machine.

#### Prerequisites
Python 3.6 or higher: Ensure you have Python installed. You can download it from python.org.


#### Clone the Repository
```bash
git clone https://github.com/b-tekinli/BeyzInfectify.git
cd BeyzInfectify
```


#### Download Malware Database
1. Visit the [Virus Share](https://virusshare.com/hashes)
2. Download the files.
3. Place these files in the hash_db/ directory of the project.



### Usage
Here's how you can use the BeyzInfectify to scan directories for malware.


#### Basic Scan
To scan a specific directory, run the following command:

```bash
python main.py --directory /path/to/your/directory
```



### Command-Line Argument
- `--directory`: Specifies the path of the directory to scan.



### Contributing
Contributions are welcome! If you'd like to contribute to the BeyzInfectify, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a Pull Request.

Please ensure your code follows the project's coding standards and includes appropriate documentation.



### Acknowledgements
- [Gözde Sarmısak](https://gozdesarmisak.com/)
- [Shuhari Researchers](https://www.linkedin.com/company/shuhari-researchers/)

