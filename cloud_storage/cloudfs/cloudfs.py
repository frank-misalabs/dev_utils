import fsspec
from typing import List, Optional

class CloudFs:
    def __init__(self, url: str, **storage_options):
        self.url = url
        self.fs = fsspec.filesystem(self._get_protocol(url), **storage_options)

    def _get_protocol(self, url: str) -> str:
        return url.split(':')[0]

    def _get_path(self, path: str) -> str:
        return f"{self.url}/{path.lstrip('/')}"

    def create_file(self, path: str, content: bytes = b"") -> None:
        with self.fs.open(self._get_path(path), 'wb') as f:
            f.write(content)

    def create_folder(self, path: str) -> None:
        self.fs.mkdirs(self._get_path(path), exist_ok=True)

    def list(self, path: str = "") -> List[str]:
        return self.fs.ls(self._get_path(path))

    def read_file(self, path: str) -> bytes:
        with self.fs.open(self._get_path(path), 'rb') as f:
            return f.read()

    def delete(self, path: str, recursive: bool = False) -> None:
        self.fs.rm(self._get_path(path), recursive=recursive)

    def update_file(self, path: str, content: bytes) -> None:
        with self.fs.open(self._get_path(path), 'wb') as f:
            f.write(content)

    def upload_file(self, path: str, local_path: str) -> None:
        with open(local_path, 'rb') as local_file:
            with self.fs.open(self._get_path(path), 'wb') as s3_file:
                s3_file.write(local_file.read())

    def download_file(self, path: str, local_path: str) -> None:
        with open(local_path, 'wb') as local_file:
            with self.fs.open(self._get_path(path), 'rb') as s3_file:
                local_file.write(s3_file.read())

