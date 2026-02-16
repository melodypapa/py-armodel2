"""DataTransformationErrorHandlingEnum enumeration."""

from enum import Enum


class DataTransformationErrorHandlingEnum(Enum):
    """AUTOSAR DataTransformationErrorHandlingEnum enumeration."""

    NOTRANSFORMERERRORHANDLING = "noTransformerErrorHandling"
    TRANSFORMERERRORHANDLING = "transformerErrorHandling"
