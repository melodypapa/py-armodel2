"""BuildActionIoElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData.sdg import (
    Sdg,
)


class BuildActionIoElement(ARObject):
    """AUTOSAR BuildActionIoElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("category", None, True, False, None),  # category
        ("ecuc_definition", None, False, False, EcucDefinitionElement),  # ecucDefinition
        ("role", None, True, False, None),  # role
        ("sdgs", None, False, True, Sdg),  # sdgs
    ]

    def __init__(self) -> None:
        """Initialize BuildActionIoElement."""
        super().__init__()
        self.category: NameToken = None
        self.ecuc_definition: Optional[EcucDefinitionElement] = None
        self.role: Optional[Identifier] = None
        self.sdgs: list[Sdg] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BuildActionIoElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionIoElement":
        """Create BuildActionIoElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BuildActionIoElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BuildActionIoElement since parent returns ARObject
        return cast("BuildActionIoElement", obj)


class BuildActionIoElementBuilder:
    """Builder for BuildActionIoElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionIoElement = BuildActionIoElement()

    def build(self) -> BuildActionIoElement:
        """Build and return BuildActionIoElement object.

        Returns:
            BuildActionIoElement instance
        """
        # TODO: Add validation
        return self._obj
