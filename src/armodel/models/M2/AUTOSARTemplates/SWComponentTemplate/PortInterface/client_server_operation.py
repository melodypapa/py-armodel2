"""ClientServerOperation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)


class ClientServerOperation(Identifiable):
    """AUTOSAR ClientServerOperation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arguments", None, False, True, ArgumentDataPrototype),  # arguments
        ("diag_arg_integrity", None, True, False, None),  # diagArgIntegrity
        ("possible_errors", None, False, True, ApplicationError),  # possibleErrors
    ]

    def __init__(self) -> None:
        """Initialize ClientServerOperation."""
        super().__init__()
        self.arguments: list[ArgumentDataPrototype] = []
        self.diag_arg_integrity: Optional[Boolean] = None
        self.possible_errors: list[ApplicationError] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClientServerOperation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperation":
        """Create ClientServerOperation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClientServerOperation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClientServerOperation since parent returns ARObject
        return cast("ClientServerOperation", obj)


class ClientServerOperationBuilder:
    """Builder for ClientServerOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperation = ClientServerOperation()

    def build(self) -> ClientServerOperation:
        """Build and return ClientServerOperation object.

        Returns:
            ClientServerOperation instance
        """
        # TODO: Add validation
        return self._obj
