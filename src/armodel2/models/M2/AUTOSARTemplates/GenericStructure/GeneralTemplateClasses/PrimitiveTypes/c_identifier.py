"""CIdentifier AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 291)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 108)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 43)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.string import (
    String,
)

# This datatype represents a string, that follows the rules of C-identifiers. Tags: xml.xsd.customType=C-IDENTIFIER xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]* xml.xsd.type=string
class CIdentifier(ARPrimitive):
    """AUTOSAR CIdentifier primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    blueprint_value: String
    name_pattern: Optional[String]

    def __init__(self, value: Optional[str] = None, blueprint_value: String = None, name_pattern: Optional[String] = None) -> None:
        """Initialize CIdentifier.

        Args:
            value: The primitive value
            blueprint_value: blueprintValue
            name_pattern: namePattern
        """
        super().__init__()
        self.value: Optional[str] = value
        self.blueprint_value: String = blueprint_value
        self.name_pattern: Optional[String] = name_pattern
