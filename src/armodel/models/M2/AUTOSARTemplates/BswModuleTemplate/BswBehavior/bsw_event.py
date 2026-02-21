"""BswEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 87)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from abc import ABC, abstractmethod


class BswEvent(AbstractEvent, ABC):
    """AUTOSAR BswEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    context_refs: list[ARRef]
    disabled_in_mode_description_instance_refs: list[ModeDeclaration]
    starts_on_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswEvent."""
        super().__init__()
        self.context_refs: list[ARRef] = []
        self.disabled_in_mode_description_instance_refs: list[ModeDeclaration] = []
        self.starts_on_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_refs (list to container "CONTEXT-REFS")
        if self.context_refs:
            wrapper = ET.Element("CONTEXT-REFS")
            for item in self.context_refs:
                serialized = SerializationHelper.serialize_item(item, "BswDistinguishedPartition")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize disabled_in_mode_description_instance_refs (list to container "DISABLED-IN-MODE-DESCRIPTION-INSTANCE-REFS")
        if self.disabled_in_mode_description_instance_refs:
            wrapper = ET.Element("DISABLED-IN-MODE-DESCRIPTION-INSTANCE-REFS")
            for item in self.disabled_in_mode_description_instance_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize starts_on_event_ref
        if self.starts_on_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.starts_on_event_ref, "BswModuleEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STARTS-ON-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEvent":
        """Deserialize XML element to BswEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEvent, cls).deserialize(element)

        # Parse context_refs (list from container "CONTEXT-REFS")
        obj.context_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-REFS")
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
                    obj.context_refs.append(child_value)

        # Parse disabled_in_mode_description_instance_refs (list from container "DISABLED-IN-MODE-DESCRIPTION-INSTANCE-REFS")
        obj.disabled_in_mode_description_instance_refs = []
        container = SerializationHelper.find_child_element(element, "DISABLED-IN-MODE-DESCRIPTION-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.disabled_in_mode_description_instance_refs.append(child_value)

        # Parse starts_on_event_ref
        child = SerializationHelper.find_child_element(element, "STARTS-ON-EVENT-REF")
        if child is not None:
            starts_on_event_ref_value = ARRef.deserialize(child)
            obj.starts_on_event_ref = starts_on_event_ref_value

        return obj



class BswEventBuilder:
    """Builder for BswEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEvent = BswEvent()

    def build(self) -> BswEvent:
        """Build and return BswEvent object.

        Returns:
            BswEvent instance
        """
        # TODO: Add validation
        return self._obj
