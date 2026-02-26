"""PositiveUnlimitedInteger AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 459)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is a positive unlimited integer which can be denoted in decimal, binary, octal and hexadecimal. Tags: xml.xsd.customType=POSITIVE-UNLIMITED-INTEGER xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+ xml.xsd.type=string Table E.65: PositiveUnlimitedInteger
class PositiveUnlimitedInteger(ARPrimitive):
    """AUTOSAR PositiveUnlimitedInteger primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize PositiveUnlimitedInteger.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
