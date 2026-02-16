"""ApplicationInterface AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface.field import (
    Field,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class ApplicationInterface(PortInterface):
    """AUTOSAR ApplicationInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("attributes", None, False, True, Field),  # attributes
        ("commands", None, False, True, ClientServerOperation),  # commands
        ("indications", None, False, True, VariableDataPrototype),  # indications
    ]

    def __init__(self) -> None:
        """Initialize ApplicationInterface."""
        super().__init__()
        self.attributes: list[Field] = []
        self.commands: list[ClientServerOperation] = []
        self.indications: list[VariableDataPrototype] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationInterface":
        """Create ApplicationInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationInterface since parent returns ARObject
        return cast("ApplicationInterface", obj)


class ApplicationInterfaceBuilder:
    """Builder for ApplicationInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationInterface = ApplicationInterface()

    def build(self) -> ApplicationInterface:
        """Build and return ApplicationInterface object.

        Returns:
            ApplicationInterface instance
        """
        # TODO: Add validation
        return self._obj
