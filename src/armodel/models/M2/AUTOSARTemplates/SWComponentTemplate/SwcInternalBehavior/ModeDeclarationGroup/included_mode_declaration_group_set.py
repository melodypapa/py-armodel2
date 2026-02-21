"""IncludedModeDeclarationGroupSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 601)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class IncludedModeDeclarationGroupSet(ARObject):
    """AUTOSAR IncludedModeDeclarationGroupSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_refs: list[ARRef]
    prefix: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize IncludedModeDeclarationGroupSet."""
        super().__init__()
        self.mode_refs: list[ARRef] = []
        self.prefix: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize IncludedModeDeclarationGroupSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize mode_refs (list to container "MODE-REFS")
        if self.mode_refs:
            wrapper = ET.Element("MODE-REFS")
            for item in self.mode_refs:
                serialized = SerializationHelper.serialize_item(item, "ModeDeclarationGroup")
                if serialized is not None:
                    child_elem = ET.Element("MODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize prefix
        if self.prefix is not None:
            serialized = SerializationHelper.serialize_item(self.prefix, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IncludedModeDeclarationGroupSet":
        """Deserialize XML element to IncludedModeDeclarationGroupSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IncludedModeDeclarationGroupSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mode_refs (list from container "MODE-REFS")
        obj.mode_refs = []
        container = SerializationHelper.find_child_element(element, "MODE-REFS")
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
                    obj.mode_refs.append(child_value)

        # Parse prefix
        child = SerializationHelper.find_child_element(element, "PREFIX")
        if child is not None:
            prefix_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.prefix = prefix_value

        return obj



class IncludedModeDeclarationGroupSetBuilder:
    """Builder for IncludedModeDeclarationGroupSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IncludedModeDeclarationGroupSet = IncludedModeDeclarationGroupSet()

    def build(self) -> IncludedModeDeclarationGroupSet:
        """Build and return IncludedModeDeclarationGroupSet object.

        Returns:
            IncludedModeDeclarationGroupSet instance
        """
        # TODO: Add validation
        return self._obj
