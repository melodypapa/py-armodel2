"""IEEE1722TpAcfBus AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 657)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from abc import ABC, abstractmethod


class IEEE1722TpAcfBus(Identifiable, ABC):
    """AUTOSAR IEEE1722TpAcfBus."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    acf_parts: list[IEEE1722TpAcfBusPart]
    bus_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBus."""
        super().__init__()
        self.acf_parts: list[IEEE1722TpAcfBusPart] = []
        self.bus_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfBus to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfBus, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acf_parts (list to container "ACF-PARTS")
        if self.acf_parts:
            wrapper = ET.Element("ACF-PARTS")
            for item in self.acf_parts:
                serialized = ARObject._serialize_item(item, "IEEE1722TpAcfBusPart")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize bus_id
        if self.bus_id is not None:
            serialized = ARObject._serialize_item(self.bus_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUS-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfBus":
        """Deserialize XML element to IEEE1722TpAcfBus object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfBus object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfBus, cls).deserialize(element)

        # Parse acf_parts (list from container "ACF-PARTS")
        obj.acf_parts = []
        container = ARObject._find_child_element(element, "ACF-PARTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.acf_parts.append(child_value)

        # Parse bus_id
        child = ARObject._find_child_element(element, "BUS-ID")
        if child is not None:
            bus_id_value = child.text
            obj.bus_id = bus_id_value

        return obj



class IEEE1722TpAcfBusBuilder:
    """Builder for IEEE1722TpAcfBus."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfBus = IEEE1722TpAcfBus()

    def build(self) -> IEEE1722TpAcfBus:
        """Build and return IEEE1722TpAcfBus object.

        Returns:
            IEEE1722TpAcfBus instance
        """
        # TODO: Add validation
        return self._obj
