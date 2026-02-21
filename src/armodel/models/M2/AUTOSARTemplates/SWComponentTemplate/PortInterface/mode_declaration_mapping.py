"""ModeDeclarationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDeclarationMapping(Identifiable):
    """AUTOSAR ModeDeclarationMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_mode_refs: list[ARRef]
    second_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeDeclarationMapping."""
        super().__init__()
        self.first_mode_refs: list[ARRef] = []
        self.second_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeDeclarationMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_mode_refs (list to container "FIRST-MODE-REFS")
        if self.first_mode_refs:
            wrapper = ET.Element("FIRST-MODE-REFS")
            for item in self.first_mode_refs:
                serialized = ARObject._serialize_item(item, "ModeDeclaration")
                if serialized is not None:
                    child_elem = ET.Element("FIRST-MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize second_mode_ref
        if self.second_mode_ref is not None:
            serialized = ARObject._serialize_item(self.second_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationMapping":
        """Deserialize XML element to ModeDeclarationMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDeclarationMapping, cls).deserialize(element)

        # Parse first_mode_refs (list from container "FIRST-MODE-REFS")
        obj.first_mode_refs = []
        container = ARObject._find_child_element(element, "FIRST-MODE-REFS")
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
                    obj.first_mode_refs.append(child_value)

        # Parse second_mode_ref
        child = ARObject._find_child_element(element, "SECOND-MODE-REF")
        if child is not None:
            second_mode_ref_value = ARRef.deserialize(child)
            obj.second_mode_ref = second_mode_ref_value

        return obj



class ModeDeclarationMappingBuilder:
    """Builder for ModeDeclarationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationMapping = ModeDeclarationMapping()

    def build(self) -> ModeDeclarationMapping:
        """Build and return ModeDeclarationMapping object.

        Returns:
            ModeDeclarationMapping instance
        """
        # TODO: Add validation
        return self._obj
