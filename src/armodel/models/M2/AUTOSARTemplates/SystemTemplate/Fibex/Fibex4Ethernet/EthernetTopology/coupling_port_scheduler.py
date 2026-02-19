"""CouplingPortScheduler AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetCouplingPortSchedulerEnum,
)


class CouplingPortScheduler(CouplingPortStructuralElement):
    """AUTOSAR CouplingPortScheduler."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    port_scheduler_scheduler_enum: Optional[EthernetCouplingPortSchedulerEnum]
    predecessors: list[CouplingPortStructuralElement]
    def __init__(self) -> None:
        """Initialize CouplingPortScheduler."""
        super().__init__()
        self.port_scheduler_scheduler_enum: Optional[EthernetCouplingPortSchedulerEnum] = None
        self.predecessors: list[CouplingPortStructuralElement] = []
    def serialize(self) -> ET.Element:
        """Serialize CouplingPortScheduler to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortScheduler, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_scheduler_scheduler_enum
        if self.port_scheduler_scheduler_enum is not None:
            serialized = ARObject._serialize_item(self.port_scheduler_scheduler_enum, "EthernetCouplingPortSchedulerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-SCHEDULER-SCHEDULER-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize predecessors (list to container "PREDECESSORS")
        if self.predecessors:
            wrapper = ET.Element("PREDECESSORS")
            for item in self.predecessors:
                serialized = ARObject._serialize_item(item, "CouplingPortStructuralElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortScheduler":
        """Deserialize XML element to CouplingPortScheduler object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortScheduler object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortScheduler, cls).deserialize(element)

        # Parse port_scheduler_scheduler_enum
        child = ARObject._find_child_element(element, "PORT-SCHEDULER-SCHEDULER-ENUM")
        if child is not None:
            port_scheduler_scheduler_enum_value = EthernetCouplingPortSchedulerEnum.deserialize(child)
            obj.port_scheduler_scheduler_enum = port_scheduler_scheduler_enum_value

        # Parse predecessors (list from container "PREDECESSORS")
        obj.predecessors = []
        container = ARObject._find_child_element(element, "PREDECESSORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.predecessors.append(child_value)

        return obj



class CouplingPortSchedulerBuilder:
    """Builder for CouplingPortScheduler."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortScheduler = CouplingPortScheduler()

    def build(self) -> CouplingPortScheduler:
        """Build and return CouplingPortScheduler object.

        Returns:
            CouplingPortScheduler instance
        """
        # TODO: Add validation
        return self._obj
