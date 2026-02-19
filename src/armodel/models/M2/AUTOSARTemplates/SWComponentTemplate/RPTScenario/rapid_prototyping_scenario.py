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

    def serialize(self) -> ET.Element:
        """Serialize RapidPrototypingScenario to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RapidPrototypingScenario, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize host_system
        if self.host_system is not None:
            serialized = ARObject._serialize_item(self.host_system, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOST-SYSTEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_containers (list to container "RPT-CONTAINERS")
        if self.rpt_containers:
            wrapper = ET.Element("RPT-CONTAINERS")
            for item in self.rpt_containers:
                serialized = ARObject._serialize_item(item, "RptContainer")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_profiles (list to container "RPT-PROFILES")
        if self.rpt_profiles:
            wrapper = ET.Element("RPT-PROFILES")
            for item in self.rpt_profiles:
                serialized = ARObject._serialize_item(item, "RptProfile")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_system
        if self.rpt_system is not None:
            serialized = ARObject._serialize_item(self.rpt_system, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SYSTEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RapidPrototypingScenario":
        """Deserialize XML element to RapidPrototypingScenario object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RapidPrototypingScenario object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RapidPrototypingScenario, cls).deserialize(element)

        # Parse host_system
        child = ARObject._find_child_element(element, "HOST-SYSTEM")
        if child is not None:
            host_system_value = ARObject._deserialize_by_tag(child, "System")
            obj.host_system = host_system_value

        # Parse rpt_containers (list from container "RPT-CONTAINERS")
        obj.rpt_containers = []
        container = ARObject._find_child_element(element, "RPT-CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_containers.append(child_value)

        # Parse rpt_profiles (list from container "RPT-PROFILES")
        obj.rpt_profiles = []
        container = ARObject._find_child_element(element, "RPT-PROFILES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_profiles.append(child_value)

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
