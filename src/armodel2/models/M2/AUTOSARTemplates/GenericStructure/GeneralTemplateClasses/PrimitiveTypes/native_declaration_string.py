"""NativeDeclarationString AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 333)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 112)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This string contains a native data declaration of a data type in a programming language. It is basically a string, but white-space shall be preserved. Tags: xml.xsd.customType=NATIVE-DECLARATION-STRING xml.xsd.type=string xml.xsd.whiteSpace=preserve Table 5.40: NativeDeclarationString
class NativeDeclarationString(ARPrimitive):
    """AUTOSAR NativeDeclarationString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize NativeDeclarationString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
