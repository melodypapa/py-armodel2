"""ConsumedProvidedServiceInstanceGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 523)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """AUTOSAR ConsumedProvidedServiceInstanceGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consumed_service_refs: list[Any]
    provided_service_refs: list[Any]
    def __init__(self) -> None:
        """Initialize ConsumedProvidedServiceInstanceGroup."""
        super().__init__()
        self.consumed_service_refs: list[Any] = []
        self.provided_service_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize ConsumedProvidedServiceInstanceGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsumedProvidedServiceInstanceGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consumed_service_refs (list to container "CONSUMED-SERVICE-REFS")
        if self.consumed_service_refs:
            wrapper = ET.Element("CONSUMED-SERVICE-REFS")
            for item in self.consumed_service_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONSUMED-SERVICE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provided_service_refs (list to container "PROVIDED-SERVICE-REFS")
        if self.provided_service_refs:
            wrapper = ET.Element("PROVIDED-SERVICE-REFS")
            for item in self.provided_service_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("PROVIDED-SERVICE-REF")
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
    def deserialize(cls, element: ET.Element) -> "ConsumedProvidedServiceInstanceGroup":
        """Deserialize XML element to ConsumedProvidedServiceInstanceGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedProvidedServiceInstanceGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsumedProvidedServiceInstanceGroup, cls).deserialize(element)

        # Parse consumed_service_refs (list from container "CONSUMED-SERVICE-REFS")
        obj.consumed_service_refs = []
        container = ARObject._find_child_element(element, "CONSUMED-SERVICE-REFS")
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
                    obj.consumed_service_refs.append(child_value)

        # Parse provided_service_refs (list from container "PROVIDED-SERVICE-REFS")
        obj.provided_service_refs = []
        container = ARObject._find_child_element(element, "PROVIDED-SERVICE-REFS")
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
                    obj.provided_service_refs.append(child_value)

        return obj



class ConsumedProvidedServiceInstanceGroupBuilder:
    """Builder for ConsumedProvidedServiceInstanceGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedProvidedServiceInstanceGroup = ConsumedProvidedServiceInstanceGroup()

    def build(self) -> ConsumedProvidedServiceInstanceGroup:
        """Build and return ConsumedProvidedServiceInstanceGroup object.

        Returns:
            ConsumedProvidedServiceInstanceGroup instance
        """
        # TODO: Add validation
        return self._obj
