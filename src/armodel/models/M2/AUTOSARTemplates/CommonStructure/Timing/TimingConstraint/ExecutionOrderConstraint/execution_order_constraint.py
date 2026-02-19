"""ExecutionOrderConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)


class ExecutionOrderConstraint(TimingConstraint):
    """AUTOSAR ExecutionOrderConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    execution_order: Optional[Any]
    ignore_order: Optional[Boolean]
    is_event: Optional[Boolean]
    ordered_elements: list[Any]
    permit_multiple: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ExecutionOrderConstraint."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.execution_order: Optional[Any] = None
        self.ignore_order: Optional[Boolean] = None
        self.is_event: Optional[Boolean] = None
        self.ordered_elements: list[Any] = []
        self.permit_multiple: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize ExecutionOrderConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutionOrderConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize execution_order
        if self.execution_order is not None:
            serialized = ARObject._serialize_item(self.execution_order, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTION-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ignore_order
        if self.ignore_order is not None:
            serialized = ARObject._serialize_item(self.ignore_order, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IGNORE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_event
        if self.is_event is not None:
            serialized = ARObject._serialize_item(self.is_event, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ordered_elements (list to container "ORDERED-ELEMENTS")
        if self.ordered_elements:
            wrapper = ET.Element("ORDERED-ELEMENTS")
            for item in self.ordered_elements:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize permit_multiple
        if self.permit_multiple is not None:
            serialized = ARObject._serialize_item(self.permit_multiple, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERMIT-MULTIPLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionOrderConstraint":
        """Deserialize XML element to ExecutionOrderConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutionOrderConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutionOrderConstraint, cls).deserialize(element)

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse execution_order
        child = ARObject._find_child_element(element, "EXECUTION-ORDER")
        if child is not None:
            execution_order_value = child.text
            obj.execution_order = execution_order_value

        # Parse ignore_order
        child = ARObject._find_child_element(element, "IGNORE-ORDER")
        if child is not None:
            ignore_order_value = child.text
            obj.ignore_order = ignore_order_value

        # Parse is_event
        child = ARObject._find_child_element(element, "IS-EVENT")
        if child is not None:
            is_event_value = child.text
            obj.is_event = is_event_value

        # Parse ordered_elements (list from container "ORDERED-ELEMENTS")
        obj.ordered_elements = []
        container = ARObject._find_child_element(element, "ORDERED-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ordered_elements.append(child_value)

        # Parse permit_multiple
        child = ARObject._find_child_element(element, "PERMIT-MULTIPLE")
        if child is not None:
            permit_multiple_value = child.text
            obj.permit_multiple = permit_multiple_value

        return obj



class ExecutionOrderConstraintBuilder:
    """Builder for ExecutionOrderConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionOrderConstraint = ExecutionOrderConstraint()

    def build(self) -> ExecutionOrderConstraint:
        """Build and return ExecutionOrderConstraint object.

        Returns:
            ExecutionOrderConstraint instance
        """
        # TODO: Add validation
        return self._obj
