"""RunnableEntityInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 956)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    base: Optional[CompositionSwComponentType]
    context_sws: list[Any]
    target_runnable: Optional[RunnableEntity]
    def __init__(self) -> None:
        """Initialize RunnableEntityInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_sws: list[Any] = []
        self.target_runnable: Optional[RunnableEntity] = None

    def serialize(self) -> ET.Element:
        """Serialize RunnableEntityInCompositionInstanceRef to XML element.

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

        # Serialize context_sws (list to container "CONTEXT-SWS")
        if self.context_sws:
            wrapper = ET.Element("CONTEXT-SWS")
            for item in self.context_sws:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_runnable
        if self.target_runnable is not None:
            serialized = ARObject._serialize_item(self.target_runnable, "RunnableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-RUNNABLE")
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

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "CompositionSwComponentType")
            obj.base = base_value

        # Parse context_sws (list from container "CONTEXT-SWS")
        obj.context_sws = []
        container = ARObject._find_child_element(element, "CONTEXT-SWS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_sws.append(child_value)

        # Parse target_runnable
        child = ARObject._find_child_element(element, "TARGET-RUNNABLE")
        if child is not None:
            target_runnable_value = ARObject._deserialize_by_tag(child, "RunnableEntity")
            obj.target_runnable = target_runnable_value

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
