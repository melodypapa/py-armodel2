"""IPSecConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 571)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config_props import (
    IPSecConfigProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_rule import (
        IPSecRule,
    )



class IPSecConfig(ARObject):
    """AUTOSAR IPSecConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ip_sec_config: Optional[IPSecConfigProps]
    ip_sec_rules: list[IPSecRule]
    def __init__(self) -> None:
        """Initialize IPSecConfig."""
        super().__init__()
        self.ip_sec_config: Optional[IPSecConfigProps] = None
        self.ip_sec_rules: list[IPSecRule] = []
    def serialize(self) -> ET.Element:
        """Serialize IPSecConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize ip_sec_config
        if self.ip_sec_config is not None:
            serialized = ARObject._serialize_item(self.ip_sec_config, "IPSecConfigProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-SEC-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_sec_rules (list to container "IP-SEC-RULES")
        if self.ip_sec_rules:
            wrapper = ET.Element("IP-SEC-RULES")
            for item in self.ip_sec_rules:
                serialized = ARObject._serialize_item(item, "IPSecRule")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecConfig":
        """Deserialize XML element to IPSecConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPSecConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ip_sec_config
        child = ARObject._find_child_element(element, "IP-SEC-CONFIG")
        if child is not None:
            ip_sec_config_value = ARObject._deserialize_by_tag(child, "IPSecConfigProps")
            obj.ip_sec_config = ip_sec_config_value

        # Parse ip_sec_rules (list from container "IP-SEC-RULES")
        obj.ip_sec_rules = []
        container = ARObject._find_child_element(element, "IP-SEC-RULES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ip_sec_rules.append(child_value)

        return obj



class IPSecConfigBuilder:
    """Builder for IPSecConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPSecConfig = IPSecConfig()

    def build(self) -> IPSecConfig:
        """Build and return IPSecConfig object.

        Returns:
            IPSecConfig instance
        """
        # TODO: Add validation
        return self._obj
