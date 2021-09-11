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
    parser.add_argument(
        "-p", "--page", help="page number", default=1
    )
    args = parser.parse_args()
    security = args.security
    output = args.output
    page = int(args.page)
    print(f"Running query for {security} page {page}")
    try:
        nasdaq_parser = Nasdaq_Institution_Page_Parser()

        df = nasdaq_parser.load_details(security=security, page=page)

        date_str = datetime.now().strftime("%Y%m%d")

        df.to_csv(
            f"{output}/nasdaq.institution.{date_str}.{security}.page{page}.csv", index=False)
    finally:
        nasdaq_parser.close()
