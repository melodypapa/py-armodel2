"""SwBaseType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2060)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type import (
    BaseType,
)


class SwBaseType(BaseType):
    """AUTOSAR SwBaseType."""

    def __init__(self) -> None:
        """Initialize SwBaseType."""
        super().__init__()

    @classmethod
    def deserialize(cls, element: ET.Element) -> SwBaseType:
        """Deserialize XML element to SwBaseType, handling both nested and flat formats.

        Handles two XML structures:
        1. Standard: <BASE-TYPE-DEFINITION> wrapper with concrete subclass
        2. Flat: Direct children (BASE-TYPE-SIZE, BASE-TYPE-ENCODING, etc.)

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwBaseType object
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
            ARObject,
        )
        from armodel.models.M2.MSR.AsamHdo.BaseTypes.base_type_direct_definition import (
            BaseTypeDirectDefinition,
        )

        # First, use parent's standard deserialize for common fields
        obj = super().deserialize(element)

        # Check for BASE-TYPE-DEFINITION wrapper (standard format)
        # Try both with and without namespace
        def_elem = element.find('BASE-TYPE-DEFINITION')
        if def_elem is None:
            # Try with namespace wildcard
            def_elem = element.find('{*}BASE-TYPE-DEFINITION')
        
        if def_elem is None:
            # Flat format: create BaseTypeDirectDefinition manually
            # Use namespace wildcard to find elements
            defn = BaseTypeDirectDefinition()
            defn.base_type_size = ARObject._extract_text(element.find('{*}BASE-TYPE-SIZE'))
            defn.base_type_encoding = ARObject._extract_text(element.find('{*}BASE-TYPE-ENCODING'))
            defn.mem_alignment = ARObject._extract_text(element.find('{*}MEM-ALIGNMENT'))
            defn.byte_order = ARObject._extract_text(element.find('{*}BYTE-ORDER'))
            defn.native = ARObject._extract_text(element.find('{*}NATIVE-DECLARATION'))

            obj.base_type_definition = defn

        return obj


class SwBaseTypeBuilder:
    """Builder for SwBaseType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwBaseType = SwBaseType()

    def build(self) -> SwBaseType:
        """Build and return SwBaseType object.

        Returns:
            SwBaseType instance
        """
        # TODO: Add validation
        return self._obj
