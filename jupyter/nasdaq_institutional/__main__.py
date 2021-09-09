import os
from nasdaq_institutional.nasdaq_institutional_analysis import Nasdaq_Institution_Page_Parser
from datetime import datetime
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--security", help="security"
    )
    parser.add_argument(
        "-o", "--output", help="output path"
    )
    args = parser.parse_args()
    security = args.security
    output = args.output

    try:
        nasdaq_parser = Nasdaq_Institution_Page_Parser()

        df = nasdaq_parser.load_details(security=security, page=1)

        date_str = datetime.now().strftime("%Y%m%d")

        df.to_csv(
            f"{output}/nasdaq.institution.{date_str}.{security}.csv", index=False)
    finally:
        nasdaq_parser.close()
