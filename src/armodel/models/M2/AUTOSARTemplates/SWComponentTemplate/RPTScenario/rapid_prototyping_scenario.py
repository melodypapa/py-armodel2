"""RapidPrototypingScenario AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_container import (
    RptContainer,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_profile import (
    RptProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class RapidPrototypingScenario(ARElement):
    """AUTOSAR RapidPrototypingScenario."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("host_system", None, False, False, System),  # hostSystem
        ("rpt_containers", None, False, True, RptContainer),  # rptContainers
        ("rpt_profiles", None, False, True, RptProfile),  # rptProfiles
        ("rpt_system", None, False, False, System),  # rptSystem
    ]

    def __init__(self) -> None:
        """Initialize RapidPrototypingScenario."""
        super().__init__()
        self.host_system: Optional[System] = None
        self.rpt_containers: list[RptContainer] = []
        self.rpt_profiles: list[RptProfile] = []
        self.rpt_system: Optional[System] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RapidPrototypingScenario to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RapidPrototypingScenario":
        """Create RapidPrototypingScenario from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RapidPrototypingScenario instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RapidPrototypingScenario since parent returns ARObject
        return cast("RapidPrototypingScenario", obj)


class RapidPrototypingScenarioBuilder:
    """Builder for RapidPrototypingScenario."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RapidPrototypingScenario = RapidPrototypingScenario()

    def build(self) -> RapidPrototypingScenario:
        """Build and return RapidPrototypingScenario object.

        Returns:
            RapidPrototypingScenario instance
        """
        # TODO: Add validation
        return self._obj
