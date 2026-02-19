"""ClientServerInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 308)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 101)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 432)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerInterface(PortInterface):
    """AUTOSAR ClientServerInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operations: list[ClientServerOperation]
    possible_errors: list[ApplicationError]
    def __init__(self) -> None:
        """Initialize ClientServerInterface."""
        super().__init__()
        self.operations: list[ClientServerOperation] = []
        self.possible_errors: list[ApplicationError] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterface":
        """Deserialize XML element to ClientServerInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterface object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse operations (list)
        obj.operations = []
        for child in ARObject._find_all_child_elements(element, "OPERATIONS"):
            operations_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operations.append(operations_value)

        # Parse possible_errors (list)
        obj.possible_errors = []
        for child in ARObject._find_all_child_elements(element, "POSSIBLE-ERRORS"):
            possible_errors_value = ARObject._deserialize_by_tag(child, "ApplicationError")
            obj.possible_errors.append(possible_errors_value)

        return obj



class ClientServerInterfaceBuilder:
    """Builder for ClientServerInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterface = ClientServerInterface()

    def build(self) -> ClientServerInterface:
        """Build and return ClientServerInterface object.

        Returns:
            ClientServerInterface instance
        """
        # TODO: Add validation
        return self._obj
