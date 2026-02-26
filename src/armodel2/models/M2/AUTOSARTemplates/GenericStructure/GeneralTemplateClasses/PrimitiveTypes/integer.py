"""Integer AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 453)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# An instance of Integer is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...). The value can be expressed in decimal, octal, hexadecimal and binary representation. Negative numbers can only be expressed in decimal notation Range is from -2147483648 and 2147483647. Tags: xml.xsd.customType=INTEGER xml.xsd.pattern=0|[\+\-]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+ xml.xsd.type=string Table E.50: Integer
class Integer(ARPrimitive):
    """AUTOSAR Integer primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = int
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[int] = None) -> None:
        """Initialize Integer.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[int] = value
