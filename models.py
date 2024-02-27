from dataclasses import dataclass
from enum import Enum
from typing import Optional, TypedDict
from dane.provenance import Provenance


# returned by callback()
class CallbackResponse(TypedDict):
    state: int
    message: str


# These are the types of output this worker (possibly) provides (depending on configuration)
class OutputType(Enum):
    AUDIO = "audio"  # produced by feature_extraction.py
    PROVENANCE = "provenance"  # produced by provenance.py

@dataclass
class AudioExtractionInput:
    state: int  # HTTP status code
    message: str  # error/success message
    source_id: str = ""  # <program ID>__<carrier ID>
    input_file_path: str = ""  # where the video was downloaded from
    provenance: Optional[Provenance] = None  # mostly: how long did it take to download


@dataclass
class AudioExtractionOutput:
    state: int  # HTTP status code
    message: str  # error/success message
    output_file_path: str = ""  # where to store the audio file
    provenance: Optional[Provenance] = None  # audio extraction provenance