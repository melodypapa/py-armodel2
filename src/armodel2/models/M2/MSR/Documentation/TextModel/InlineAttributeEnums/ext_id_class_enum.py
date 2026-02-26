"""ExtIdClassEnum AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 317)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is in fact an enumerator. The possible values are all legal XML names of identifiable objects even those of other XML files. If the schemas of all questionable files are generated from a common meta-model, this is something like an IdentifiableSubtypesEnum. Maybe a future version of the Schema generator can generate such an enum. As of now it is specified as string. Tags: xml.xsd.customType=EXT-ID-CLASS-ENUM xml.xsd.type=string Table 9.35: ExtIdClassEnum
class ExtIdClassEnum(ARPrimitive):
    """AUTOSAR ExtIdClassEnum primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize ExtIdClassEnum.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
