"""BswModuleCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_distinguished_partition import (
    BswDistinguishedPartition,
)
from abc import ABC, abstractmethod


class BswModuleCallPoint(Referrable, ABC):
    """AUTOSAR BswModuleCallPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    context_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BswModuleCallPoint."""
        super().__init__()
        self.context_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BswModuleCallPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleCallPoint, self).serialize()

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
                serialized = ARObject._serialize_item(item, "BswDistinguishedPartition")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleCallPoint":
        """Deserialize XML element to BswModuleCallPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleCallPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleCallPoint, cls).deserialize(element)

        # Parse context_refs (list from container "CONTEXT-REFS")
        obj.context_refs = []
        container = ARObject._find_child_element(element, "CONTEXT-REFS")
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
                    obj.context_refs.append(child_value)

        return obj



class BswModuleCallPointBuilder:
    """Builder for BswModuleCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleCallPoint = BswModuleCallPoint()

    def build(self) -> BswModuleCallPoint:
        """Build and return BswModuleCallPoint object.

        Returns:
            BswModuleCallPoint instance
        """
        # TODO: Add validation
        return self._obj
