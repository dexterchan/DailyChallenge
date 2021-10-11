from __future__ import annotations
import boto3
from typing import Dict, Protocol
import os
import json
from shutil import copyfile
import traceback

from .loghelper import get_logger, logging
logger = get_logger(__name__, logging.DEBUG)

def get_aws_boto3_s3(credential_filename:str):
    with open(credential_filename) as f:
        line = f.readline()
    access_id, secret_key = line.split(":")
    session = boto3.Session(
        aws_access_key_id=access_id,
        aws_secret_access_key=secret_key
    )
    return session.resource("s3")


class State_IO(Protocol):
    """
        Read and write Json State from an IO source: e.g. file
    """
    @classmethod
    def instantiate(self, filename) -> State_IO:
        """
            Create a State_IO object to 
            1) read Dict from IO
            2) write Dict into IO
        """
        s3prefix = "s3://"
        if filename[:len(s3prefix)] == s3prefix:
            return S3_State_IO(
                s3_path=filename
            )
        else:
            return File_State_IO(
                file_name=filename
            )
    def read(self) -> Dict:
        pass
    def write(self, data:Dict) -> bool:
        pass

class File_State_IO(State_IO):
    def __init__(self, file_name:str) -> None:
        self.file_name = file_name

    def read(self) -> Dict:
        obj = {}
        try:
            if os.path.isfile(self.file_name):
                with open(self.file_name, "r") as f:
                    obj = json.load(f)
        except Exception as e:
            logger.error(traceback.format_exc())
            logger.info("Failed to load state, switch to blank")
            obj = {}
        return obj

    def write(self, data:Dict) -> bool:
        #logger.debug(data)
        if os.path.exists(self.file_name):
            copyfile(self.file_name, self.file_name+".backup")
        with open(self.file_name, "w") as f:
            json.dump(data, f)

class S3_State_IO(State_IO):
    def __init__(self, s3_path:str) -> None:
        self.s3_path = s3_path

    def read() -> Dict:
        pass
    def write() -> bool:
        pass


