#!/usr/bin/python3

from collections import defaultdict
import signal
import sys

def signal_handler(sig, frame):
        print_stats()

        def print_stats():
                global total_size, status_codes
                    print(f"Total file size: {total_size}")
                        for code in sorted(status_codes.keys()):
                                    print(f"{code}: {status_codes[code]}")
                                        sys.exit(0)

                                        total_size = 0
                                        status_codes = defaultdict(int)
                                        lines_processed = 0

                                        signal.signal(signal.SIGINT, signal_handler)

                                        try:
                                                for line in sys.stdin:
                                                            line = line.strip()
                                                                    parts = line.split()
                                                                            if len(parts) != 7:
                                                                                            continue

                                                                                                ip, date, req, status_code, file_size = parts
                                                                                                        if not status_code.isdigit():
                                                                                                                        continue

                                                                                                                            file_size = int(file_size)
                                                                                                                                    total_size += file_size
                                                                                                                                            status_codes[status_code] += 1
                                                                                                                                                    lines_processed += 1

                                                                                                                                                            if lines_processed % 10 == 0:
                                                                                                                                                                            print_stats()

                                        except KeyboardInterrupt:
                                                print_stats()
