"""SomeipTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 619)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_connection import (
    SomeipTpConnection,
)


class SomeipTpConfig(TpConfig):
    """AUTOSAR SomeipTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_channels: list[SomeipTpChannel]
    tp_connections: list[SomeipTpConnection]
    def __init__(self) -> None:
        """Initialize SomeipTpConfig."""
        super().__init__()
        self.tp_channels: list[SomeipTpChannel] = []
        self.tp_connections: list[SomeipTpConnection] = []

    def serialize(self) -> ET.Element:
        """Serialize SomeipTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_channels (list to container "TP-CHANNELS")
        if self.tp_channels:
            wrapper = ET.Element("TP-CHANNELS")
            for item in self.tp_channels:
                serialized = ARObject._serialize_item(item, "SomeipTpChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = ARObject._serialize_item(item, "SomeipTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpConfig":
        """Deserialize XML element to SomeipTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipTpConfig, cls).deserialize(element)

        # Parse tp_channels (list from container "TP-CHANNELS")
        obj.tp_channels = []
        container = ARObject._find_child_element(element, "TP-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_channels.append(child_value)

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = ARObject._find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

        return obj



class SomeipTpConfigBuilder:
    """Builder for SomeipTpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipTpConfig = SomeipTpConfig()

    def build(self) -> SomeipTpConfig:
        """Build and return SomeipTpConfig object.

        Returns:
            SomeipTpConfig instance
        """
        # TODO: Add validation
        return self._obj
