"""SwAddrMethod AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 144)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 413)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_AuxillaryObjects.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import (
    MemoryAllocationKeywordPolicyType,
    MemorySectionType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    SectionInitializationPolicyType,
)


class SwAddrMethod(ARElement):
    """AUTOSAR SwAddrMethod."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    memory: Optional[MemoryAllocationKeywordPolicyType]
    options: list[Identifier]
    section: Optional[SectionInitializationPolicyType]
    section_type: Optional[MemorySectionType]
    def __init__(self) -> None:
        """Initialize SwAddrMethod."""
        super().__init__()
        self.memory: Optional[MemoryAllocationKeywordPolicyType] = None
        self.options: list[Identifier] = []
        self.section: Optional[SectionInitializationPolicyType] = None
        self.section_type: Optional[MemorySectionType] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAddrMethod":
        """Deserialize XML element to SwAddrMethod object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAddrMethod object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse memory
        child = ARObject._find_child_element(element, "MEMORY")
        if child is not None:
            memory_value = child.text
            obj.memory = memory_value

        # Parse options (list)
        obj.options = []
        for child in ARObject._find_all_child_elements(element, "OPTIONS"):
            options_value = child.text
            obj.options.append(options_value)

        # Parse section
        child = ARObject._find_child_element(element, "SECTION")
        if child is not None:
            section_value = child.text
            obj.section = section_value

        # Parse section_type
        child = ARObject._find_child_element(element, "SECTION-TYPE")
        if child is not None:
            section_type_value = child.text
            obj.section_type = section_type_value

        return obj



class SwAddrMethodBuilder:
    """Builder for SwAddrMethod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAddrMethod = SwAddrMethod()

    def build(self) -> SwAddrMethod:
        """Build and return SwAddrMethod object.

        Returns:
            SwAddrMethod instance
        """
        # TODO: Add validation
        return self._obj
