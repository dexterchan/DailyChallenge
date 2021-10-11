from tictactoe.io import S3_State_IO, State_IO
from typing import Dict
import logging

logging.basicConfig(
    format="%(asctime)-15s %(levelname)s %(message)s (%(filename)s:%(lineno)s)")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

read_s3_path = "s3://boar-tradingbot/state/game.statistics.json"
write_s3_path = "s3://boar-tradingbot/state/game.statistics.copycat.json"

read_state_io = State_IO.instantiate(
    filename=read_s3_path
)

org_data:Dict = read_state_io.read()

assert len(org_data) > 0

write_state_io = State_IO.instantiate(filename=write_s3_path)
write_state_io.write(data=org_data)


read_state_io2 = State_IO.instantiate(filename=write_s3_path)
validate_data:Dict = read_state_io2.read()

assert org_data == validate_data






