"""IEEE1722TpAcfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 656)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_connection import (
    IEEE1722TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    """AUTOSAR IEEE1722TpAcfConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    acf_transporteds: list[IEEE1722TpAcfBus]
    collection: Optional[TimeValue]
    mixed_bus_type: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfConnection."""
        super().__init__()
        self.acf_transporteds: list[IEEE1722TpAcfBus] = []
        self.collection: Optional[TimeValue] = None
        self.mixed_bus_type: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acf_transporteds (list to container "ACF-TRANSPORTEDS")
        if self.acf_transporteds:
            wrapper = ET.Element("ACF-TRANSPORTEDS")
            for item in self.acf_transporteds:
                serialized = ARObject._serialize_item(item, "IEEE1722TpAcfBus")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize collection
        if self.collection is not None:
            serialized = ARObject._serialize_item(self.collection, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mixed_bus_type
        if self.mixed_bus_type is not None:
            serialized = ARObject._serialize_item(self.mixed_bus_type, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIXED-BUS-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfConnection":
        """Deserialize XML element to IEEE1722TpAcfConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfConnection, cls).deserialize(element)

        # Parse acf_transporteds (list from container "ACF-TRANSPORTEDS")
        obj.acf_transporteds = []
        container = ARObject._find_child_element(element, "ACF-TRANSPORTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acf_transporteds.append(child_value)

        # Parse collection
        child = ARObject._find_child_element(element, "COLLECTION")
        if child is not None:
            collection_value = child.text
            obj.collection = collection_value

        # Parse mixed_bus_type
        child = ARObject._find_child_element(element, "MIXED-BUS-TYPE")
        if child is not None:
            mixed_bus_type_value = child.text
            obj.mixed_bus_type = mixed_bus_type_value

        return obj



class IEEE1722TpAcfConnectionBuilder:
    """Builder for IEEE1722TpAcfConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfConnection = IEEE1722TpAcfConnection()

    def build(self) -> IEEE1722TpAcfConnection:
        """Build and return IEEE1722TpAcfConnection object.

        Returns:
            IEEE1722TpAcfConnection instance
        """
        # TODO: Add validation
        return self._obj
