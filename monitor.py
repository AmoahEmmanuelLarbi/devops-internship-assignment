from pathlib import Path
from datetime import datetime


def log_directory_files():

    # get target directory
    # use parent directory of this file as the target directory
    target_directory = Path(__file__).resolve().parent

    try:
        # ensure target is a directory
        if not target_directory.exists():
            raise FileNotFoundError("The target path does not exist.")

        if not target_directory.is_dir():
            raise NotADirectoryError("The target path must be a directory.")

        print(f"Scanning target folder {target_directory} ...")

        # open file with context manager
        with open("log.txt", "w", encoding="utf-8") as logfile:

            logfile.write(
                "FILE NAME \t\t\t | FILE SIZE IN KB \t\t | FILE TIMESTAMP (MM:DD:YY H:M:S)\n"
            )
            logfile.write("-" * 75 + "\n")

            # get all files in the target directory
            # loop through the files in the directory and log to a file
            for file in target_directory.iterdir():
                if file.is_file():

                    # ignore log.txt
                    if file.name == "log.txt":
                        continue
                    # get file name
                    filename = file.name

                    # get file size in KB
                    file_info = file.stat()
                    file_size_in_bytes = file_info.st_size
                    file_size_in_kb = file_size_in_bytes / 1024

                    # get file timestamp
                    timestamp = file_info.st_mtime
                    file_timestamp = datetime.fromtimestamp(timestamp)
                    file_timestamp = file_timestamp.strftime("%m-%d-%Y %H:%M:%S")

                    # write to file(log.txt)
                    logfile.write(
                        f"{filename:<20} \t\t | {file_size_in_kb:.2f} KB \t | {file_timestamp:>24}\n"
                    )

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except NotADirectoryError as e:
        print(f"Error: {e}")


def main():
    log_directory_files()


if __name__ == "__main__"():
    main()
