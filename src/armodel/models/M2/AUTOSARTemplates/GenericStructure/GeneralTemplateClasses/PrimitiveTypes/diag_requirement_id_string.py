"""DiagRequirementIdString AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 754)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 109)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This string denotes an Identifier for a requirement. Tags: xml.xsd.customType=DIAG-REQUIREMENT-ID-STRING xml.xsd.pattern=[0-9a-zA-Z_\-]+ xml.xsd.type=string Table 13.16: DiagRequirementIdString
class DiagRequirementIdString(ARPrimitive):
    """AUTOSAR DiagRequirementIdString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize DiagRequirementIdString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
