"""RevisionLabelString AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 113)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This primitive represents an internal AUTOSAR revision label which identifies an engineering object. It represents a pattern which • supports three integers representing from left to right MajorVersion, MinorVersion, PatchVersion. • may add an application specific suffix separated by one of ".", "_", ";". Legal patterns are for example: • 4.0.0 • 4.0.0.1234565 • 4.0.0_vendor specific;13 • 4.0.0;12 Tags: xml.xsd.customType=REVISION-LABEL-STRING xml.xsd.pattern=[0-9]+\.[0-9]+\.[0-9]+([\._;].*)? xml.xsd.type=string Table 4.61: RevisionLabelString
class RevisionLabelString(ARPrimitive):
    """AUTOSAR RevisionLabelString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize RevisionLabelString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
