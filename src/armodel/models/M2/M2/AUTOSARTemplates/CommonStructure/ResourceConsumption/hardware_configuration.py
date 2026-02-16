"""HardwareConfiguration AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class HardwareConfiguration(ARObject):
    """AUTOSAR HardwareConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "additional": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # additional
        "processor_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # processorMode
        "processor_speed": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # processorSpeed
    }

    def __init__(self) -> None:
        """Initialize HardwareConfiguration."""
        super().__init__()
        self.additional: Optional[String] = None
        self.processor_mode: Optional[String] = None
        self.processor_speed: Optional[String] = None


class HardwareConfigurationBuilder:
    """Builder for HardwareConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HardwareConfiguration = HardwareConfiguration()

    def build(self) -> HardwareConfiguration:
        """Build and return HardwareConfiguration object.

        Returns:
            HardwareConfiguration instance
        """
        # TODO: Add validation
        return self._obj
