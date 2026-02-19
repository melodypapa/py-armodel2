"""RapidPrototypingScenario AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 846)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    host_system: Optional[System]
    rpt_containers: list[RptContainer]
    rpt_profiles: list[RptProfile]
    rpt_system: Optional[System]
    def __init__(self) -> None:
        """Initialize RapidPrototypingScenario."""
        super().__init__()
        self.host_system: Optional[System] = None
        self.rpt_containers: list[RptContainer] = []
        self.rpt_profiles: list[RptProfile] = []
        self.rpt_system: Optional[System] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RapidPrototypingScenario":
        """Deserialize XML element to RapidPrototypingScenario object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RapidPrototypingScenario object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse host_system
        child = ARObject._find_child_element(element, "HOST-SYSTEM")
        if child is not None:
            host_system_value = ARObject._deserialize_by_tag(child, "System")
            obj.host_system = host_system_value

        # Parse rpt_containers (list)
        obj.rpt_containers = []
        for child in ARObject._find_all_child_elements(element, "RPT-CONTAINERS"):
            rpt_containers_value = ARObject._deserialize_by_tag(child, "RptContainer")
            obj.rpt_containers.append(rpt_containers_value)

        # Parse rpt_profiles (list)
        obj.rpt_profiles = []
        for child in ARObject._find_all_child_elements(element, "RPT-PROFILES"):
            rpt_profiles_value = ARObject._deserialize_by_tag(child, "RptProfile")
            obj.rpt_profiles.append(rpt_profiles_value)

        # Parse rpt_system
        child = ARObject._find_child_element(element, "RPT-SYSTEM")
        if child is not None:
            rpt_system_value = ARObject._deserialize_by_tag(child, "System")
            obj.rpt_system = rpt_system_value

        return obj



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
