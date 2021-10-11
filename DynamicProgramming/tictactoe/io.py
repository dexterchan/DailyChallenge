from __future__ import annotations
import boto3
from typing import Dict, Protocol
import os
import json
from shutil import copyfile
import traceback

from botocore.exceptions import ClientError

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
    s3_prefix = "s3://"
    def __init__(self, s3_path:str) -> None:
        self.client=boto3.client("s3")
        self.s3_path = s3_path
        #Head object to check if object exists
        p = s3_path[len(self.s3_prefix):] if s3_path[:len(self.s3_prefix)] == self.s3_prefix else s3_path
        import re
        matcher = re.compile(r"^([^/]+)/(.*[^/])$")
        m = matcher.match(p)
        if m is None:
            raise Exception ("INvalid s3 path")
        self.bucket = m.group(1)
        self.prefix = m.group(2)
        

    def _check_file_object_exist(self, bucket:str, prefix:str) -> bool:
        try:
            response = self.client.head_object(
                Bucket=bucket,
                Key=prefix
            )
            return True
        except ClientError as ce:
            logger.info(ce)
        return False

    def read(self) -> Dict:
        if not self._check_file_object_exist(bucket=self.bucket, prefix=self.prefix):
            return {}
        response = self.client.get_object(
            Bucket=self.bucket,
            Key=self.prefix
        )
        json_str = response["Body"].read().decode("utf-8")
        return json.loads(json_str)

    def write(self, data:Dict) -> bool:
        payload = json.dumps(data).encode("utf-8")
        try:
            self.client.put_object(
                Bucket=self.bucket,
                Key=self.prefix,
                Body=payload
            )
            return True
        except ClientError as e:
            logger.error(e)
        return False


