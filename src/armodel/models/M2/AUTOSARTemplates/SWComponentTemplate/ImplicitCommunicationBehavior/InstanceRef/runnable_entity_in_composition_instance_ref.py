"""RunnableEntityInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 956)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class RunnableEntityInCompositionInstanceRef(ARObject):
    """AUTOSAR RunnableEntityInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base_ref: Optional[ARRef]
    context_sw_refs: list[Any]
    target_runnable_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RunnableEntityInCompositionInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_sw_refs: list[Any] = []
        self.target_runnable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RunnableEntityInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "CompositionSwComponentType")
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

        # Serialize context_sw_refs (list to container "CONTEXT-SW-REFS")
        if self.context_sw_refs:
            wrapper = ET.Element("CONTEXT-SW-REFS")
            for item in self.context_sw_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-SW-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_runnable_ref
        if self.target_runnable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_runnable_ref, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-RUNNABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntityInCompositionInstanceRef":
        """Deserialize XML element to RunnableEntityInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RunnableEntityInCompositionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base_ref
        child = SerializationHelper.find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_sw_refs (list from container "CONTEXT-SW-REFS")
        obj.context_sw_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-SW-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_sw_refs.append(child_value)

        # Parse target_runnable_ref
        child = SerializationHelper.find_child_element(element, "TARGET-RUNNABLE-REF")
        if child is not None:
            target_runnable_ref_value = ARRef.deserialize(child)
            obj.target_runnable_ref = target_runnable_ref_value

        return obj



class RunnableEntityInCompositionInstanceRefBuilder:
    """Builder for RunnableEntityInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityInCompositionInstanceRef = RunnableEntityInCompositionInstanceRef()

    def build(self) -> RunnableEntityInCompositionInstanceRef:
        """Build and return RunnableEntityInCompositionInstanceRef object.

        Returns:
            RunnableEntityInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
