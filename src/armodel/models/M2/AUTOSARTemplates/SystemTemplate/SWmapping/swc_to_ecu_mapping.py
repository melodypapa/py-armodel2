"""SwcToEcuMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

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


class SwcToEcuMapping(Identifiable):
    """AUTOSAR SwcToEcuMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    components: list[Any]
    controlled_hw_ref: Optional[ARRef]
    ecu_instance_ref: Optional[ARRef]
    processing_unit_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcToEcuMapping."""
        super().__init__()
        self.components: list[Any] = []
        self.controlled_hw_ref: Optional[ARRef] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.processing_unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcToEcuMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcToEcuMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize components (list to container "COMPONENTS")
        if self.components:
            wrapper = ET.Element("COMPONENTS")
            for item in self.components:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize controlled_hw_ref
        if self.controlled_hw_ref is not None:
            serialized = ARObject._serialize_item(self.controlled_hw_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTROLLED-HW-REF")
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

        # Serialize processing_unit_ref
        if self.processing_unit_ref is not None:
            serialized = ARObject._serialize_item(self.processing_unit_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToEcuMapping":
        """Deserialize XML element to SwcToEcuMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToEcuMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcToEcuMapping, cls).deserialize(element)

        # Parse components (list from container "COMPONENTS")
        obj.components = []
        container = ARObject._find_child_element(element, "COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.components.append(child_value)

        # Parse controlled_hw_ref
        child = ARObject._find_child_element(element, "CONTROLLED-HW-REF")
        if child is not None:
            controlled_hw_ref_value = ARRef.deserialize(child)
            obj.controlled_hw_ref = controlled_hw_ref_value

        # Parse ecu_instance_ref
        child = ARObject._find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse processing_unit_ref
        child = ARObject._find_child_element(element, "PROCESSING-UNIT-REF")
        if child is not None:
            processing_unit_ref_value = ARRef.deserialize(child)
            obj.processing_unit_ref = processing_unit_ref_value

        return obj



class SwcToEcuMappingBuilder:
    """Builder for SwcToEcuMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToEcuMapping = SwcToEcuMapping()

    def build(self) -> SwcToEcuMapping:
        """Build and return SwcToEcuMapping object.

        Returns:
            SwcToEcuMapping instance
        """
        # TODO: Add validation
        return self._obj
