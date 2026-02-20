"""CouplingPortShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 123)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_structural_element import (
    CouplingPortStructuralElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port_fifo import (
    CouplingPortFifo,
)


class CouplingPortShaper(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    idle_slope: Optional[PositiveInteger]
    predecessor_fifo: CouplingPortFifo
    def __init__(self) -> None:
        """Initialize CouplingPortShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.predecessor_fifo: CouplingPortFifo = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortShaper to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortShaper, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize idle_slope
        if self.idle_slope is not None:
            serialized = ARObject._serialize_item(self.idle_slope, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDLE-SLOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize predecessor_fifo
        if self.predecessor_fifo is not None:
            serialized = ARObject._serialize_item(self.predecessor_fifo, "CouplingPortFifo")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREDECESSOR-FIFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortShaper":
        """Deserialize XML element to CouplingPortShaper object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortShaper object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortShaper, cls).deserialize(element)

        # Parse idle_slope
        child = ARObject._find_child_element(element, "IDLE-SLOPE")
        if child is not None:
            idle_slope_value = child.text
            obj.idle_slope = idle_slope_value

        # Parse predecessor_fifo
        child = ARObject._find_child_element(element, "PREDECESSOR-FIFO")
        if child is not None:
            predecessor_fifo_value = ARObject._deserialize_by_tag(child, "CouplingPortFifo")
            obj.predecessor_fifo = predecessor_fifo_value

        return obj



class CouplingPortShaperBuilder:
    """Builder for CouplingPortShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortShaper = CouplingPortShaper()

    def build(self) -> CouplingPortShaper:
        """Build and return CouplingPortShaper object.

        Returns:
            CouplingPortShaper instance
        """
        # TODO: Add validation
        return self._obj
