"""ECUMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)


class ECUMapping(Identifiable):
    """AUTOSAR ECUMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "comm_controllers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (Communication),
        ),  # commControllers
        "ecu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwElement,
        ),  # ecu
        "ecu_instance": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcuInstance,
        ),  # ecuInstance
        "hw_port_mapping": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=HwPortMapping,
        ),  # hwPortMapping
    }

    def __init__(self) -> None:
        """Initialize ECUMapping."""
        super().__init__()
        self.comm_controllers: list[Any] = []
        self.ecu: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.hw_port_mapping: HwPortMapping = None


class ECUMappingBuilder:
    """Builder for ECUMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ECUMapping = ECUMapping()

    def build(self) -> ECUMapping:
        """Build and return ECUMapping object.

        Returns:
            ECUMapping instance
        """
        # TODO: Add validation
        return self._obj
