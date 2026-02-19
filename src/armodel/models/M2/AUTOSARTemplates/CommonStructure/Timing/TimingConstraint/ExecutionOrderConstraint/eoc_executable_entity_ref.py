"""EOCExecutableEntityRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 120)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)


class EOCExecutableEntityRef(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module: Optional[BswImplementation]
    component: Optional[Any]
    executable_entity: Optional[ExecutableEntity]
    successors: list[Any]
    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRef."""
        super().__init__()
        self.bsw_module: Optional[BswImplementation] = None
        self.component: Optional[Any] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.successors: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EOCExecutableEntityRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EOCExecutableEntityRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module
        if self.bsw_module is not None:
            serialized = ARObject._serialize_item(self.bsw_module, "BswImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize component
        if self.component is not None:
            serialized = ARObject._serialize_item(self.component, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize executable_entity
        if self.executable_entity is not None:
            serialized = ARObject._serialize_item(self.executable_entity, "ExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTABLE-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize successors (list to container "SUCCESSORS")
        if self.successors:
            wrapper = ET.Element("SUCCESSORS")
            for item in self.successors:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRef":
        """Deserialize XML element to EOCExecutableEntityRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCExecutableEntityRef, cls).deserialize(element)

        # Parse bsw_module
        child = ARObject._find_child_element(element, "BSW-MODULE")
        if child is not None:
            bsw_module_value = ARObject._deserialize_by_tag(child, "BswImplementation")
            obj.bsw_module = bsw_module_value

        # Parse component
        child = ARObject._find_child_element(element, "COMPONENT")
        if child is not None:
            component_value = child.text
            obj.component = component_value

        # Parse executable_entity
        child = ARObject._find_child_element(element, "EXECUTABLE-ENTITY")
        if child is not None:
            executable_entity_value = ARObject._deserialize_by_tag(child, "ExecutableEntity")
            obj.executable_entity = executable_entity_value

        # Parse successors (list from container "SUCCESSORS")
        obj.successors = []
        container = ARObject._find_child_element(element, "SUCCESSORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.successors.append(child_value)

        return obj



class EOCExecutableEntityRefBuilder:
    """Builder for EOCExecutableEntityRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRef = EOCExecutableEntityRef()

    def build(self) -> EOCExecutableEntityRef:
        """Build and return EOCExecutableEntityRef object.

        Returns:
            EOCExecutableEntityRef instance
        """
        # TODO: Add validation
        return self._obj
