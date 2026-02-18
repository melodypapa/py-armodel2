"""AnyVersionString AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# Tags: xml.xsd.customType=ANY-VERSION-STRING xml.xsd.pattern=[0-9]+|ANY xml.xsd.type=string Table E.7: AnyVersionString
class AnyVersionString(ARPrimitive):
    """AUTOSAR AnyVersionString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize AnyVersionString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
