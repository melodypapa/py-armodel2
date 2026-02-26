"""NameToken AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 324)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 456)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is an identifier as used in xml, e.g. xml-names. Typical usages are, for example, the names of type emitters, protocols, or profiles. For details see NMTOKEN definition on the W3C website (https://www.w3.org/TR/xml/#NT-Nmtoken). Note: Although NameToken supports a wide range of characters, the actually allowed patterns for a certain attribute typed by NameToken may be further restricted by the specification of that attribute. Tags: xml.xsd.customType=NMTOKEN-STRING xml.xsd.type=NMTOKEN Table C.38: NameToken
class NameToken(ARPrimitive):
    """AUTOSAR NameToken primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize NameToken.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
