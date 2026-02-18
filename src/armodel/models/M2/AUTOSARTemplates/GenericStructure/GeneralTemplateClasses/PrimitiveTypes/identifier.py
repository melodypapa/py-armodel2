"""Identifier AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 299)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 61)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 42)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# An Identifier is a string with a number of constraints on its appearance, satisfying the requirements typical programming languages define for their Identifiers. This datatype represents a string, that can be used as a c-Identifier. It shall start with a letter, may consist of letters, digits and underscores. Tags: xml.xsd.customType=IDENTIFIER xml.xsd.maxLength=128 xml.xsd.pattern=[a-zA-Z][a-zA-Z0-9_]* xml.xsd.type=string
class Identifier(ARPrimitive):
    """AUTOSAR Identifier primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize Identifier.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
