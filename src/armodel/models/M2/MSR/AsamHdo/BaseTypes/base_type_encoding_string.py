"""BaseTypeEncodingString AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 291)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 108)

JSON Source: packages/M2_MSR_AsamHdo_BaseTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is the string denotion of a BaseType encoding. It may be refined by specific use-cases. Tags: xml.xsd.customType=BASE-TYPE-ENCODING-STRING xml.xsd.type=string Table 5.25: BaseTypeEncodingString
class BaseTypeEncodingString(ARPrimitive):
    """AUTOSAR BaseTypeEncodingString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize BaseTypeEncodingString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
