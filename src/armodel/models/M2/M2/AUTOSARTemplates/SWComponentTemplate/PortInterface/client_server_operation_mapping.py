"""ClientServerOperationMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)


class ClientServerOperationMapping(ARObject):
    """AUTOSAR ClientServerOperationMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataPrototypeMapping,
        ),  # arguments
        "first_operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # firstOperation
        "first_to_second": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DataTransformation,
        ),  # firstToSecond
        "second": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # second
    }

    def __init__(self) -> None:
        """Initialize ClientServerOperationMapping."""
        super().__init__()
        self.arguments: list[DataPrototypeMapping] = []
        self.first_operation: Optional[ClientServerOperation] = None
        self.first_to_second: Optional[DataTransformation] = None
        self.second: Optional[ClientServerOperation] = None


class ClientServerOperationMappingBuilder:
    """Builder for ClientServerOperationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationMapping = ClientServerOperationMapping()

    def build(self) -> ClientServerOperationMapping:
        """Build and return ClientServerOperationMapping object.

        Returns:
            ClientServerOperationMapping instance
        """
        # TODO: Add validation
        return self._obj
