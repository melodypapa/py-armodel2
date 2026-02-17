"""UserDefinedTransformationDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 771)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)


class UserDefinedTransformationDescription(TransformationDescription):
    """AUTOSAR UserDefinedTransformationDescription."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize UserDefinedTransformationDescription."""
        super().__init__()


class UserDefinedTransformationDescriptionBuilder:
    """Builder for UserDefinedTransformationDescription."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedTransformationDescription = UserDefinedTransformationDescription()

    def build(self) -> UserDefinedTransformationDescription:
        """Build and return UserDefinedTransformationDescription object.

        Returns:
            UserDefinedTransformationDescription instance
        """
        # TODO: Add validation
        return self._obj
