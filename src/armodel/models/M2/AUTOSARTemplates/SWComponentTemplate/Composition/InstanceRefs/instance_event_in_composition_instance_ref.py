"""InstanceEventInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 959)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class InstanceEventInCompositionInstanceRef(ARObject):
    """AUTOSAR InstanceEventInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: Optional[CompositionSwComponentType]
    context_prototypes: list[Any]
    target_event: Optional[RTEEvent]
    def __init__(self) -> None:
        """Initialize InstanceEventInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_prototypes: list[Any] = []
        self.target_event: Optional[RTEEvent] = None
    def serialize(self) -> ET.Element:
        """Serialize InstanceEventInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

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

        # Serialize context_prototypes (list to container "CONTEXT-PROTOTYPES")
        if self.context_prototypes:
            wrapper = ET.Element("CONTEXT-PROTOTYPES")
            for item in self.context_prototypes:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_event
        if self.target_event is not None:
            serialized = ARObject._serialize_item(self.target_event, "RTEEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstanceEventInCompositionInstanceRef":
        """Deserialize XML element to InstanceEventInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InstanceEventInCompositionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse context_prototypes (list from container "CONTEXT-PROTOTYPES")
        obj.context_prototypes = []
        container = ARObject._find_child_element(element, "CONTEXT-PROTOTYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_prototypes.append(child_value)

        # Parse target_event
        child = ARObject._find_child_element(element, "TARGET-EVENT")
        if child is not None:
            target_event_value = ARObject._deserialize_by_tag(child, "RTEEvent")
            obj.target_event = target_event_value

        return obj



class InstanceEventInCompositionInstanceRefBuilder:
    """Builder for InstanceEventInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstanceEventInCompositionInstanceRef = InstanceEventInCompositionInstanceRef()

    def build(self) -> InstanceEventInCompositionInstanceRef:
        """Build and return InstanceEventInCompositionInstanceRef object.

        Returns:
            InstanceEventInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
