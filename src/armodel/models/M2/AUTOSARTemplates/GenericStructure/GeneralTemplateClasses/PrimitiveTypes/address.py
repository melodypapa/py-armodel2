"""Address AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 107)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is used to specify an address within the CPU. Tags: xml.xsd.customType=ADDRESS xml.xsd.pattern=0[xX][0-9a-fA-F]+ xml.xsd.type=string Table 4.40: Address
class Address(ARPrimitive):
    """AUTOSAR Address primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize Address.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
