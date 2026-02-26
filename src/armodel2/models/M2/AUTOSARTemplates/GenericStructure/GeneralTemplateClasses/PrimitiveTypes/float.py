"""Float AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 223)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 448)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# An instance of Float is an element from the set of real numbers. Tags: xml.xsd.customType=FLOAT xml.xsd.type=double Table D.25: Float
class Float(ARPrimitive):
    """AUTOSAR Float primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = float
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[float] = None) -> None:
        """Initialize Float.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[float] = value
