"""AlignmentType AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 144)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 419)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 107)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This primitive represents the alignment of objects within a memory section. The value is in number of bits or UNKNOWN (deprecated), 8 , 16, 32, 64 UNSPECIFIED, BOOLEAN, or PTR. Typical values for numbers are 8, 16, 32, 64. Tags: xml.xsd.customType=ALIGNMENT-TYPE xml.xsd.pattern=[1-9][0-9]*|0[xX][0-9a-fA-F]*|0[bB] [0-1]+|0[0-7]*|UNSPECIFIED|UNKNOWN|BOOLEAN|PTR xml.xsd.type=string Table 8.3: AlignmentType
class AlignmentType(ARPrimitive):
    """AUTOSAR AlignmentType primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize AlignmentType.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
