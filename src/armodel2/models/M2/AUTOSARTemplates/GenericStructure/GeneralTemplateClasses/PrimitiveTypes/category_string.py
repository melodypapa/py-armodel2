"""CategoryString AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 109)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This represents the pattern applicable to categories. It is basically the same as Identifier but has a different semantics. Therefore it is modeled as a primitive of its own. Tags: xml.xsd.customType=CATEGORY-STRING xml.xsd.pattern=[a-zA-Z][a-zA-Z0-9_]* xml.xsd.type=string Table 4.47: CategoryString
class CategoryString(ARPrimitive):
    """AUTOSAR CategoryString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize CategoryString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
