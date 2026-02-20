"""SecurityEventStateFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)


class SecurityEventStateFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventStateFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_if_state_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SecurityEventStateFilter."""
        super().__init__()
        self.block_if_state_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventStateFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventStateFilter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize block_if_state_refs (list to container "BLOCK-IF-STATE-REFS")
        if self.block_if_state_refs:
            wrapper = ET.Element("BLOCK-IF-STATE-REFS")
            for item in self.block_if_state_refs:
                serialized = ARObject._serialize_item(item, "BlockState")
                if serialized is not None:
                    child_elem = ET.Element("BLOCK-IF-STATE-REF")
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
    def deserialize(cls, element: ET.Element) -> "SecurityEventStateFilter":
        """Deserialize XML element to SecurityEventStateFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventStateFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventStateFilter, cls).deserialize(element)

        # Parse block_if_state_refs (list from container "BLOCK-IF-STATE-REFS")
        obj.block_if_state_refs = []
        container = ARObject._find_child_element(element, "BLOCK-IF-STATE-REFS")
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
                    obj.block_if_state_refs.append(child_value)

        return obj



class SecurityEventStateFilterBuilder:
    """Builder for SecurityEventStateFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventStateFilter = SecurityEventStateFilter()

    def build(self) -> SecurityEventStateFilter:
        """Build and return SecurityEventStateFilter object.

        Returns:
            SecurityEventStateFilter instance
        """
        # TODO: Add validation
        return self._obj
