"""AssignNad AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class AssignNad(LinConfigurationEntry):
    """AUTOSAR AssignNad."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("new_nad", None, True, False, None),  # newNad
    ]

    def __init__(self) -> None:
        """Initialize AssignNad."""
        super().__init__()
        self.new_nad: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AssignNad to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssignNad":
        """Create AssignNad from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AssignNad instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AssignNad since parent returns ARObject
        return cast("AssignNad", obj)


class AssignNadBuilder:
    """Builder for AssignNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignNad = AssignNad()

    def build(self) -> AssignNad:
        """Build and return AssignNad object.

        Returns:
            AssignNad instance
        """
        # TODO: Add validation
        return self._obj
