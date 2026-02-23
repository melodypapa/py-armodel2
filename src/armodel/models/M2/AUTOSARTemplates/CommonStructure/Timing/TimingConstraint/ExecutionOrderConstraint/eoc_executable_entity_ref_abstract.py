"""EOCExecutableEntityRefAbstract AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from abc import ABC, abstractmethod


class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """AUTOSAR EOCExecutableEntityRefAbstract."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    direct_successor_refs: list[Any]
    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefAbstract."""
        super().__init__()
        self.direct_successor_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EOCExecutableEntityRefAbstract to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EOCExecutableEntityRefAbstract, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direct_successor_refs (list to container "DIRECT-SUCCESSOR-REFS")
        if self.direct_successor_refs:
            wrapper = ET.Element("DIRECT-SUCCESSOR-REFS")
            for item in self.direct_successor_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("DIRECT-SUCCESSOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefAbstract":
        """Deserialize XML element to EOCExecutableEntityRefAbstract object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRefAbstract object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCExecutableEntityRefAbstract, cls).deserialize(element)

        # Parse direct_successor_refs (list from container "DIRECT-SUCCESSOR-REFS")
        obj.direct_successor_refs = []
        container = SerializationHelper.find_child_element(element, "DIRECT-SUCCESSOR-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.direct_successor_refs.append(child_value)

        return obj



