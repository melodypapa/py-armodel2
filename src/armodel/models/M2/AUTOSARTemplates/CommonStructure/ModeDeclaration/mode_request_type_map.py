"""ModeRequestTypeMap AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
    AbstractImplementationDataType,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeRequestTypeMap(ARObject):
    """AUTOSAR ModeRequestTypeMap."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("implementation", None, False, False, AbstractImplementationDataType),  # implementation
        ("mode_group", None, False, False, ModeDeclarationGroup),  # modeGroup
    ]

    def __init__(self) -> None:
        """Initialize ModeRequestTypeMap."""
        super().__init__()
        self.implementation: Optional[AbstractImplementationDataType] = None
        self.mode_group: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeRequestTypeMap to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeRequestTypeMap":
        """Create ModeRequestTypeMap from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeRequestTypeMap instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeRequestTypeMap since parent returns ARObject
        return cast("ModeRequestTypeMap", obj)


class ModeRequestTypeMapBuilder:
    """Builder for ModeRequestTypeMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeRequestTypeMap = ModeRequestTypeMap()

    def build(self) -> ModeRequestTypeMap:
        """Build and return ModeRequestTypeMap object.

        Returns:
            ModeRequestTypeMap instance
        """
        # TODO: Add validation
        return self._obj
