"""MemorySectionLocation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.memory_section import (
    MemorySection,
)


class MemorySectionLocation(ARObject):
    """AUTOSAR MemorySectionLocation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "provided_memory": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwElement,
        ),  # providedMemory
        "software": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MemorySection,
        ),  # software
    }

    def __init__(self) -> None:
        """Initialize MemorySectionLocation."""
        super().__init__()
        self.provided_memory: Optional[HwElement] = None
        self.software: Optional[MemorySection] = None


class MemorySectionLocationBuilder:
    """Builder for MemorySectionLocation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MemorySectionLocation = MemorySectionLocation()

    def build(self) -> MemorySectionLocation:
        """Build and return MemorySectionLocation object.

        Returns:
            MemorySectionLocation instance
        """
        # TODO: Add validation
        return self._obj
