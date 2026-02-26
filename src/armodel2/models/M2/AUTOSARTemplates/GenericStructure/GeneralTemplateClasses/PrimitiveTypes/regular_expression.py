"""RegularExpression AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 112)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is a regular expression as defined in http://www.w3.org/TR/xmlschema-2 As of now it is still produced as a string in XSD. Tags: xml.xsd.customType=REGULAR-EXPRESSION xml.xsd.type=string Table 4.60: RegularExpression 112 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11
class RegularExpression(ARPrimitive):
    """AUTOSAR RegularExpression primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize RegularExpression.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
