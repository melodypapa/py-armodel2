"""SwcToSwcOperationArguments AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class SwcToSwcOperationArguments(ARObject):
    """AUTOSAR SwcToSwcOperationArguments."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "direction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (SwcToSwcOperation),
        ),  # direction
        "operations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ClientServerOperation,
        ),  # operations
    }

    def __init__(self) -> None:
        """Initialize SwcToSwcOperationArguments."""
        super().__init__()
        self.direction: Optional[Any] = None
        self.operations: list[ClientServerOperation] = []


class SwcToSwcOperationArgumentsBuilder:
    """Builder for SwcToSwcOperationArguments."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToSwcOperationArguments = SwcToSwcOperationArguments()

    def build(self) -> SwcToSwcOperationArguments:
        """Build and return SwcToSwcOperationArguments object.

        Returns:
            SwcToSwcOperationArguments instance
        """
        # TODO: Add validation
        return self._obj
