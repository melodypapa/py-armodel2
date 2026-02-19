"""SomeipSdClientServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2058)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)


class SomeipSdClientServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdClientServiceInstanceConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_find_behavior: Optional[InitialSdDelayConfig]
    priority: Optional[PositiveInteger]
    service_find: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipSdClientServiceInstanceConfig."""
        super().__init__()
        self.initial_find_behavior: Optional[InitialSdDelayConfig] = None
        self.priority: Optional[PositiveInteger] = None
        self.service_find: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipSdClientServiceInstanceConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipSdClientServiceInstanceConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_find_behavior
        if self.initial_find_behavior is not None:
            serialized = ARObject._serialize_item(self.initial_find_behavior, "InitialSdDelayConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-FIND-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_find
        if self.service_find is not None:
            serialized = ARObject._serialize_item(self.service_find, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-FIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdClientServiceInstanceConfig":
        """Deserialize XML element to SomeipSdClientServiceInstanceConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdClientServiceInstanceConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdClientServiceInstanceConfig, cls).deserialize(element)

        # Parse initial_find_behavior
        child = ARObject._find_child_element(element, "INITIAL-FIND-BEHAVIOR")
        if child is not None:
            initial_find_behavior_value = ARObject._deserialize_by_tag(child, "InitialSdDelayConfig")
            obj.initial_find_behavior = initial_find_behavior_value

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse service_find
        child = ARObject._find_child_element(element, "SERVICE-FIND")
        if child is not None:
            service_find_value = child.text
            obj.service_find = service_find_value

        return obj



class SomeipSdClientServiceInstanceConfigBuilder:
    """Builder for SomeipSdClientServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdClientServiceInstanceConfig = SomeipSdClientServiceInstanceConfig()

    def build(self) -> SomeipSdClientServiceInstanceConfig:
        """Build and return SomeipSdClientServiceInstanceConfig object.

        Returns:
            SomeipSdClientServiceInstanceConfig instance
        """
        # TODO: Add validation
        return self._obj
