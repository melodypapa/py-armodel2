"""ECUMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)


class ECUMapping(Identifiable):
    """AUTOSAR ECUMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    comm_controllers: list[Any]
    ecu_ref: Optional[ARRef]
    ecu_instance_ref: Optional[ARRef]
    hw_port_mapping_ref: ARRef
    def __init__(self) -> None:
        """Initialize ECUMapping."""
        super().__init__()
        self.comm_controllers: list[Any] = []
        self.ecu_ref: Optional[ARRef] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.hw_port_mapping_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize ECUMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ECUMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_controllers (list to container "COMM-CONTROLLERS")
        if self.comm_controllers:
            wrapper = ET.Element("COMM-CONTROLLERS")
            for item in self.comm_controllers:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_ref
        if self.ecu_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_port_mapping_ref
        if self.hw_port_mapping_ref is not None:
            serialized = ARObject._serialize_item(self.hw_port_mapping_ref, "HwPortMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-PORT-MAPPING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ECUMapping":
        """Deserialize XML element to ECUMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ECUMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ECUMapping, cls).deserialize(element)

        # Parse comm_controllers (list from container "COMM-CONTROLLERS")
        obj.comm_controllers = []
        container = ARObject._find_child_element(element, "COMM-CONTROLLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.comm_controllers.append(child_value)

        # Parse ecu_ref
        child = ARObject._find_child_element(element, "ECU-REF")
        if child is not None:
            ecu_ref_value = ARRef.deserialize(child)
            obj.ecu_ref = ecu_ref_value

        # Parse ecu_instance_ref
        child = ARObject._find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse hw_port_mapping_ref
        child = ARObject._find_child_element(element, "HW-PORT-MAPPING-REF")
        if child is not None:
            hw_port_mapping_ref_value = ARRef.deserialize(child)
            obj.hw_port_mapping_ref = hw_port_mapping_ref_value

        return obj



class ECUMappingBuilder:
    """Builder for ECUMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ECUMapping = ECUMapping()

    def build(self) -> ECUMapping:
        """Build and return ECUMapping object.

        Returns:
            ECUMapping instance
        """
        # TODO: Add validation
        return self._obj
