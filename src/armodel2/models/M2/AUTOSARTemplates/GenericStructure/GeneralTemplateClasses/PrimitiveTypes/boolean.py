"""Boolean AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 425)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# A Boolean value denotes a logical condition that is either ’true’ or ’false’. It can be one of "0", "1", "true", "false" Tags: xml.xsd.customType=BOOLEAN xml.xsd.pattern=0|1|true|false xml.xsd.type=string Table D.8: Boolean
class Boolean(ARPrimitive):
    """AUTOSAR Boolean primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = bool
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[bool] = None) -> None:
        """Initialize Boolean.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[bool] = value
