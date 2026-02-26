"""Ref AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 318)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 31)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 460)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.identifier import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.positive_integer import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.string import (
    String,
)

# This primitive denotes a name based reference. For detailed syntax see the xsd.pattern. • first slash (relative or absolute reference) [optional] • Identifier [required] • a sequence of slashes and Identifiers [optional] This primitive is used by the meta-model tools to create the references. Tags: xml.xsd.customType=REF xml.xsd.pattern=/?[a-zA-Z][a-zA-Z0-9_]{0,127}(/[a-zA-Z][a-zA-Z0-9_]{0,127})* xml.xsd.type=string
class Ref(ARPrimitive):
    """AUTOSAR Ref primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    base: Optional[Identifier]
    blueprint_value: Optional[String]
    index: Optional[PositiveInteger]

    def __init__(self, value: Optional[str] = None, base: Optional[Identifier] = None, blueprint_value: Optional[String] = None, index: Optional[PositiveInteger] = None) -> None:
        """Initialize Ref.

        Args:
            value: The primitive value
            base: base
            blueprint_value: blueprintValue
            index: index
        """
        super().__init__()
        self.value: Optional[str] = value
        self.base: Optional[Identifier] = base
        self.blueprint_value: Optional[String] = blueprint_value
        self.index: Optional[PositiveInteger] = index
