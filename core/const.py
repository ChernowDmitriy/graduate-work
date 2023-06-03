from pathlib import Path

from fastapi import Depends

from infrastructures.utils import has_access

EMPTY_VALUE = ''
BASE_DIR = Path(__file__).resolve().parent.parent
PROTECTED = [Depends(has_access)]
