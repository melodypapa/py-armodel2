"""UserDefinedTransformationProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class UserDefinedTransformationProps(TransformationProps):
    """AUTOSAR UserDefinedTransformationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationProps."""
        super().__init__()


class UserDefinedTransformationPropsBuilder:
    """Builder for UserDefinedTransformationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationProps = UserDefinedTransformationProps()

    def build(self) -> UserDefinedTransformationProps:
        """Build and return UserDefinedTransformationProps object.

        Returns:
            UserDefinedTransformationProps instance
        """
        # TODO: Add validation
        return self._obj
