"""VerbatimString AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 316)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 32)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 114)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This primitive represents a string in which white-space needs to be preserved. Tags: xml.xsd.customType=VERBATIM-STRING xml.xsd.type=string xml.xsd.whiteSpace=preserve
class VerbatimString(ARPrimitive):
    """AUTOSAR VerbatimString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize VerbatimString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
