"""McdIdentifier AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 111)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This primitive denotes a name used for measurement and calibration systems and shall follow the restrictions for an ASAM ASAP2 ident. For detailed syntax see the xsd.pattern. The size limitations are not captured. McdIdentifiers are random names which may contain characters A through Z, a through z, underscore (_), numerals 0 through 9, points (’.’) and brackets ( ’[’,’]’ ). However, the following limitations apply: the first character shall be a letter or an underscore, brackets shall occur in pairs at the end of a partial string and shall contain a number or an alpha-numerical string (description of the index of an array element). Tags: xml.xsd.customType=MCD-IDENTIFIER xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*(\.[a-zA-Z_][a-z A-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*)* xml.xsd.type=string Table 4.54: McdIdentifier
class McdIdentifier(ARPrimitive):
    """AUTOSAR McdIdentifier primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize McdIdentifier.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
