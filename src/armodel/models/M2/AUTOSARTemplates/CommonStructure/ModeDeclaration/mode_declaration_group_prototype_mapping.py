"""ModeDeclarationGroupPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototypeMapping(ARObject):
    """AUTOSAR ModeDeclarationGroupPrototypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_mode_group_prototype_ref: Optional[ARRef]
    mode_ref: Optional[ARRef]
    second_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototypeMapping."""
        super().__init__()
        self.first_mode_group_prototype_ref: Optional[ARRef] = None
        self.mode_ref: Optional[ARRef] = None
        self.second_mode_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeDeclarationGroupPrototypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize first_mode_group_prototype_ref
        if self.first_mode_group_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_mode_group_prototype_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-MODE-GROUP-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_ref
        if self.mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_mode_ref
        if self.second_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_mode_ref, "ModeDeclarationGroup")
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
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroupPrototypeMapping":
        """Deserialize XML element to ModeDeclarationGroupPrototypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationGroupPrototypeMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_mode_group_prototype_ref
        child = SerializationHelper.find_child_element(element, "FIRST-MODE-GROUP-PROTOTYPE-REF")
        if child is not None:
            first_mode_group_prototype_ref_value = ARRef.deserialize(child)
            obj.first_mode_group_prototype_ref = first_mode_group_prototype_ref_value

        # Parse mode_ref
        child = SerializationHelper.find_child_element(element, "MODE-REF")
        if child is not None:
            mode_ref_value = ARRef.deserialize(child)
            obj.mode_ref = mode_ref_value

        # Parse second_mode_ref
        child = SerializationHelper.find_child_element(element, "SECOND-MODE-REF")
        if child is not None:
            second_mode_ref_value = ARRef.deserialize(child)
            obj.second_mode_ref = second_mode_ref_value

        return obj



class ModeDeclarationGroupPrototypeMappingBuilder:
    """Builder for ModeDeclarationGroupPrototypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroupPrototypeMapping = ModeDeclarationGroupPrototypeMapping()

    def build(self) -> ModeDeclarationGroupPrototypeMapping:
        """Build and return ModeDeclarationGroupPrototypeMapping object.

        Returns:
            ModeDeclarationGroupPrototypeMapping instance
        """
        # TODO: Add validation
        return self._obj
