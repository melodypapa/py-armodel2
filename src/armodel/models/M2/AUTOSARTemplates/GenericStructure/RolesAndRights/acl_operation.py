"""AclOperation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class AclOperation(ARElement):
    """AUTOSAR AclOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implied_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize AclOperation."""
        super().__init__()
        self.implied_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize AclOperation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclOperation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implied_refs (list to container "IMPLIED-REFS")
        if self.implied_refs:
            wrapper = ET.Element("IMPLIED-REFS")
            for item in self.implied_refs:
                serialized = ARObject._serialize_item(item, "AclOperation")
                if serialized is not None:
                    child_elem = ET.Element("IMPLIED-REF")
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
    def deserialize(cls, element: ET.Element) -> "AclOperation":
        """Deserialize XML element to AclOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclOperation, cls).deserialize(element)

        # Parse implied_refs (list from container "IMPLIED-REFS")
        obj.implied_refs = []
        container = ARObject._find_child_element(element, "IMPLIED-REFS")
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
                    obj.implied_refs.append(child_value)

        return obj



class AclOperationBuilder:
    """Builder for AclOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AclOperation = AclOperation()

    def build(self) -> AclOperation:
        """Build and return AclOperation object.

        Returns:
            AclOperation instance
        """
        # TODO: Add validation
        return self._obj
