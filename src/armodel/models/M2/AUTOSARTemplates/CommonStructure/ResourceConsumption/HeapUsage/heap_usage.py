"""HeapUsage AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)


class HeapUsage(Identifiable):
    """AUTOSAR HeapUsage."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "hardware": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HardwareConfiguration,
        ),  # hardware
        "hw_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwElement,
        ),  # hwElement
        "software_context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SoftwareContext,
        ),  # softwareContext
    }

    def __init__(self) -> None:
        """Initialize HeapUsage."""
        super().__init__()
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element: Optional[HwElement] = None
        self.software_context: Optional[SoftwareContext] = None


class HeapUsageBuilder:
    """Builder for HeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HeapUsage = HeapUsage()

    def build(self) -> HeapUsage:
        """Build and return HeapUsage object.

        Returns:
            HeapUsage instance
        """
        # TODO: Add validation
        return self._obj
