"""DdsCpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 525)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_domain import (
    DdsCpDomain,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)


class DdsCpConfig(ARElement):
    """AUTOSAR DdsCpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dds_domains: list[DdsCpDomain]
    dds_qos_profiles: list[DdsCpQosProfile]
    def __init__(self) -> None:
        """Initialize DdsCpConfig."""
        super().__init__()
        self.dds_domains: list[DdsCpDomain] = []
        self.dds_qos_profiles: list[DdsCpQosProfile] = []
    def serialize(self) -> ET.Element:
        """Serialize DdsCpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dds_domains (list to container "DDS-DOMAINS")
        if self.dds_domains:
            wrapper = ET.Element("DDS-DOMAINS")
            for item in self.dds_domains:
                serialized = ARObject._serialize_item(item, "DdsCpDomain")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dds_qos_profiles (list to container "DDS-QOS-PROFILES")
        if self.dds_qos_profiles:
            wrapper = ET.Element("DDS-QOS-PROFILES")
            for item in self.dds_qos_profiles:
                serialized = ARObject._serialize_item(item, "DdsCpQosProfile")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsCpConfig":
        """Deserialize XML element to DdsCpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpConfig, cls).deserialize(element)

        # Parse dds_domains (list from container "DDS-DOMAINS")
        obj.dds_domains = []
        container = ARObject._find_child_element(element, "DDS-DOMAINS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dds_domains.append(child_value)

        # Parse dds_qos_profiles (list from container "DDS-QOS-PROFILES")
        obj.dds_qos_profiles = []
        container = ARObject._find_child_element(element, "DDS-QOS-PROFILES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dds_qos_profiles.append(child_value)

        return obj



class DdsCpConfigBuilder:
    """Builder for DdsCpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpConfig = DdsCpConfig()

    def build(self) -> DdsCpConfig:
        """Build and return DdsCpConfig object.

        Returns:
            DdsCpConfig instance
        """
        # TODO: Add validation
        return self._obj
