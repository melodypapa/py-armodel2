"""InstanceEventInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 959)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    base_ref: Optional[ARRef]
    context_prototype_refs: list[Any]
    target_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize InstanceEventInCompositionInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_prototype_refs: list[Any] = []
        self.target_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize InstanceEventInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = ARObject._serialize_item(self.base_ref, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_prototype_refs (list to container "CONTEXT-PROTOTYPE-REFS")
        if self.context_prototype_refs:
            wrapper = ET.Element("CONTEXT-PROTOTYPE-REFS")
            for item in self.context_prototype_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-PROTOTYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_event_ref
        if self.target_event_ref is not None:
            serialized = ARObject._serialize_item(self.target_event_ref, "RTEEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-EVENT-REF")
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

        # Parse base_ref
        child = ARObject._find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_prototype_refs (list from container "CONTEXT-PROTOTYPE-REFS")
        obj.context_prototype_refs = []
        container = ARObject._find_child_element(element, "CONTEXT-PROTOTYPE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_prototype_refs.append(child_value)

        # Parse target_event_ref
        child = ARObject._find_child_element(element, "TARGET-EVENT-REF")
        if child is not None:
            target_event_ref_value = ARRef.deserialize(child)
            obj.target_event_ref = target_event_ref_value

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
