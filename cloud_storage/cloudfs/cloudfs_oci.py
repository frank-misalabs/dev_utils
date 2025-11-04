import ocifs
from typing import List, Optional

class OCICloudFs:
    def __init__(self, namespace: str, bucket: str, config_file: str):
        self.namespace = namespace
        self.bucket = bucket
        self.base_uri = f"{bucket}@{namespace}"
        self.fs = ocifs.OCIFileSystem(config_file)

    def _get_path(self, path: str) -> str:
        return f"{self.base_uri}/{path.lstrip('/')}"

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
            with self.fs.open(self._get_path(path), 'wb') as oci_file:
                oci_file.write(local_file.read())

    def download_file(self, path: str, local_path: str) -> None:
        with open(local_path, 'wb') as local_file:
            with self.fs.open(self._get_path(path), 'rb') as oci_file:
                local_file.write(oci_file.read())

