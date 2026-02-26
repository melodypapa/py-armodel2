"""SymbolString AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 114)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.string import (
    String,
)

# This meta-class has the ability to contain a string plus an additional namePattern. Please note that this meta-class has only been introduced to fix an issue with the backwards compatibility between R4.0.3 and R4.1.1 in the context of McDataInstance Tags: xml.xsd.customType=SYMBOL-STRING xml.xsd.type=string
class SymbolString(ARPrimitive):
    """AUTOSAR SymbolString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    name_pattern: String

    def __init__(self, value: Optional[str] = None, name_pattern: String = None) -> None:
        """Initialize SymbolString.

        Args:
            value: The primitive value
            name_pattern: namePattern
        """
        super().__init__()
        self.value: Optional[str] = value
        self.name_pattern: String = name_pattern
