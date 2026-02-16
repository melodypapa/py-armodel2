"""RapidPrototypingScenario AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "host_system": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=System,
        ),  # hostSystem
        "rpt_containers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptContainer,
        ),  # rptContainers
        "rpt_profiles": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptProfile,
        ),  # rptProfiles
        "rpt_system": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=System,
        ),  # rptSystem
    }

    def __init__(self) -> None:
        """Initialize RapidPrototypingScenario."""
        super().__init__()
        self.host_system: Optional[System] = None
        self.rpt_containers: list[RptContainer] = []
        self.rpt_profiles: list[RptProfile] = []
        self.rpt_system: Optional[System] = None


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
