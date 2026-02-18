"""String AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1006)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2060)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 113)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This represents a String in which white-space shall be normalized before processing. For example: in order to compare two Strings: • leading and trailing white-space needs to be removed • consecutive white-space (blank, cr, lf, tab) needs to be replaced by one blank. Tags: xml.xsd.customType=STRING xml.xsd.type=string Table D.65: String 336 of 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module Description Template AUTOSAR CP R23-11
class String(ARPrimitive):
    """AUTOSAR String primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize String.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
