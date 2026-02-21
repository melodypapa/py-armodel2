"""CouplingPortFifo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortFifo(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortFifo."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_traffic: PositiveInteger
    minimum_fifo: Optional[PositiveInteger]
    shaper: Optional[Any]
    def __init__(self) -> None:
        """Initialize CouplingPortFifo."""
        super().__init__()
        self.assigned_traffic: PositiveInteger = None
        self.minimum_fifo: Optional[PositiveInteger] = None
        self.shaper: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortFifo to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortFifo, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_traffic
        if self.assigned_traffic is not None:
            serialized = SerializationHelper.serialize_item(self.assigned_traffic, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSIGNED-TRAFFIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_fifo
        if self.minimum_fifo is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_fifo, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-FIFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize shaper
        if self.shaper is not None:
            serialized = SerializationHelper.serialize_item(self.shaper, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHAPER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortFifo":
        """Deserialize XML element to CouplingPortFifo object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortFifo object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortFifo, cls).deserialize(element)

        # Parse assigned_traffic
        child = SerializationHelper.find_child_element(element, "ASSIGNED-TRAFFIC")
        if child is not None:
            assigned_traffic_value = child.text
            obj.assigned_traffic = assigned_traffic_value

        # Parse minimum_fifo
        child = SerializationHelper.find_child_element(element, "MINIMUM-FIFO")
        if child is not None:
            minimum_fifo_value = child.text
            obj.minimum_fifo = minimum_fifo_value

        # Parse shaper
        child = SerializationHelper.find_child_element(element, "SHAPER")
        if child is not None:
            shaper_value = child.text
            obj.shaper = shaper_value

        return obj



class CouplingPortFifoBuilder:
    """Builder for CouplingPortFifo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortFifo = CouplingPortFifo()

    def build(self) -> CouplingPortFifo:
        """Build and return CouplingPortFifo object.

        Returns:
            CouplingPortFifo instance
        """
        # TODO: Add validation
        return self._obj
