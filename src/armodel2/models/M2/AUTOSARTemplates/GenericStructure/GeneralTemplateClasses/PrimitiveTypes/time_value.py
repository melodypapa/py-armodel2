"""TimeValue AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 350)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 478)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This primitive type is taken for expressing time values. The numerical value is supposed to be interpreted in the physical unit second. Tags: xml.xsd.customType=TIME-VALUE xml.xsd.type=double Table D.76: TimeValue
class TimeValue(ARPrimitive):
    """AUTOSAR TimeValue primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = float
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[float] = None) -> None:
        """Initialize TimeValue.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[float] = value
