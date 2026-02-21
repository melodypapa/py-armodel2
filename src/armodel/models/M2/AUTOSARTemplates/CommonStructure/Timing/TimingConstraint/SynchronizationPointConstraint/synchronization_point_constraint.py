"""SynchronizationPointConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationPointConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)


class SynchronizationPointConstraint(TimingConstraint):
    """AUTOSAR SynchronizationPointConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    source_eec_refs: list[Any]
    source_event_refs: list[ARRef]
    target_eec_refs: list[Any]
    target_event_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SynchronizationPointConstraint."""
        super().__init__()
        self.source_eec_refs: list[Any] = []
        self.source_event_refs: list[ARRef] = []
        self.target_eec_refs: list[Any] = []
        self.target_event_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SynchronizationPointConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SynchronizationPointConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize source_eec_refs (list to container "SOURCE-EEC-REFS")
        if self.source_eec_refs:
            wrapper = ET.Element("SOURCE-EEC-REFS")
            for item in self.source_eec_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("SOURCE-EEC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_event_refs (list to container "SOURCE-EVENT-REFS")
        if self.source_event_refs:
            wrapper = ET.Element("SOURCE-EVENT-REFS")
            for item in self.source_event_refs:
                serialized = ARObject._serialize_item(item, "AbstractEvent")
                if serialized is not None:
                    child_elem = ET.Element("SOURCE-EVENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_eec_refs (list to container "TARGET-EEC-REFS")
        if self.target_eec_refs:
            wrapper = ET.Element("TARGET-EEC-REFS")
            for item in self.target_eec_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("TARGET-EEC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_event_refs (list to container "TARGET-EVENT-REFS")
        if self.target_event_refs:
            wrapper = ET.Element("TARGET-EVENT-REFS")
            for item in self.target_event_refs:
                serialized = ARObject._serialize_item(item, "AbstractEvent")
                if serialized is not None:
                    child_elem = ET.Element("TARGET-EVENT-REF")
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
    def deserialize(cls, element: ET.Element) -> "SynchronizationPointConstraint":
        """Deserialize XML element to SynchronizationPointConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SynchronizationPointConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SynchronizationPointConstraint, cls).deserialize(element)

        # Parse source_eec_refs (list from container "SOURCE-EEC-REFS")
        obj.source_eec_refs = []
        container = ARObject._find_child_element(element, "SOURCE-EEC-REFS")
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
                    obj.source_eec_refs.append(child_value)

        # Parse source_event_refs (list from container "SOURCE-EVENT-REFS")
        obj.source_event_refs = []
        container = ARObject._find_child_element(element, "SOURCE-EVENT-REFS")
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
                    obj.source_event_refs.append(child_value)

        # Parse target_eec_refs (list from container "TARGET-EEC-REFS")
        obj.target_eec_refs = []
        container = ARObject._find_child_element(element, "TARGET-EEC-REFS")
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
                    obj.target_eec_refs.append(child_value)

        # Parse target_event_refs (list from container "TARGET-EVENT-REFS")
        obj.target_event_refs = []
        container = ARObject._find_child_element(element, "TARGET-EVENT-REFS")
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
                    obj.target_event_refs.append(child_value)

        return obj



class SynchronizationPointConstraintBuilder:
    """Builder for SynchronizationPointConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronizationPointConstraint = SynchronizationPointConstraint()

    def build(self) -> SynchronizationPointConstraint:
        """Build and return SynchronizationPointConstraint object.

        Returns:
            SynchronizationPointConstraint instance
        """
        # TODO: Add validation
        return self._obj
