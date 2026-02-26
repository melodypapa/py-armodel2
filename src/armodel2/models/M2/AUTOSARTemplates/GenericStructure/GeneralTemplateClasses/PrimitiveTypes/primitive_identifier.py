"""PrimitiveIdentifier AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 112)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This meta-class has the ability to contain a string. Please note that this meta-class has only been introduced to fix an issue with the generation of attributes on primitives in context with [TPS_XMLSPR_00024]. Tags: xml.xsd.customType=PRIMITIVE-IDENTIFIER xml.xsd.maxLength=128 xml.xsd.pattern=[a-zA-Z]([a-zA-Z0-9]|_[a-zA-Z0-9])*_? xml.xsd.type=string Table 4.58: PrimitiveIdentifier
class PrimitiveIdentifier(ARPrimitive):
    """AUTOSAR PrimitiveIdentifier primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize PrimitiveIdentifier.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
