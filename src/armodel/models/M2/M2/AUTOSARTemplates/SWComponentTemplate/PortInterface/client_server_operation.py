"""ClientServerOperation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ArgumentDataPrototype,
        ),  # arguments
        "diag_arg_integrity": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # diagArgIntegrity
        "possible_errors": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationError,
        ),  # possibleErrors
    }

    def __init__(self) -> None:
        """Initialize ClientServerOperation."""
        super().__init__()
        self.arguments: list[ArgumentDataPrototype] = []
        self.diag_arg_integrity: Optional[Boolean] = None
        self.possible_errors: list[ApplicationError] = []


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
