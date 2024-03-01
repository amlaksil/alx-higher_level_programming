#!/usr/bin/python3
"""
This module calculates statistics based on input data provided in a specific
format. It reads the input line by line, and after every 10 lines or when
interrupted by a keyboard interruption (Ctrl+C), it displays the following
statistics:
    - Total file size: The sum of all file sizes encountered so far.
    - Number of lines by status code: The count of each status code encountered
      so far, grouped by status code.
Input Format
- The module expects the input data to be provided in the following format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import sys

if __name__ == '__main__':
    status_code_counts = {}
    total_size = line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) < 7:
                continue
            size = int(parts[-1])
            status_code = parts[-2]
            total_size += size
            try:
                int(status_code)
            except Exception as e:
                continue

            status_code_counts[status_code] = status_code_counts.get(
                status_code, 0) + 1

            if line_count % 10 == 0:
                print(f'File size: {total_size}')
                for code in sorted(status_code_counts.keys()):
                    if status_code_counts[code] != 0:
                        print(f'{code}: {status_code_counts[code]}')
    except KeyboardInterrupt:
        print(f'File size: {total_size}')
        for code in sorted(status_code_counts.keys()):
            if status_code_counts[code] != 0:
                print(f'{code}: {status_code_counts[code]}')
    finally:
        print(f'File size: {total_size}')
        for code in sorted(status_code_counts.keys()):
            if status_code_counts[code] != 0:
                print(f'{code}: {status_code_counts[code]}')
