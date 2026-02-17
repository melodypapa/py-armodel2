"""SwAddrMethod AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 144)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 413)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_AuxillaryObjects.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "memory": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MemoryAllocationKeywordPolicyType,
        ),  # memory
        "options": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # options
        "section": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # section
        "section_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MemorySectionType,
        ),  # sectionType
    }

    def __init__(self) -> None:
        """Initialize SwAddrMethod."""
        super().__init__()
        self.memory: Optional[MemoryAllocationKeywordPolicyType] = None
        self.options: list[Identifier] = []
        self.section: Optional[SectionInitializationPolicyType] = None
        self.section_type: Optional[MemorySectionType] = None


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
