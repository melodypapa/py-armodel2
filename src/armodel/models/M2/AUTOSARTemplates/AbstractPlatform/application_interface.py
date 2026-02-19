"""ApplicationInterface AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AbstractPlatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attributes: list[Field]
    commands: list[ClientServerOperation]
    indication_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ApplicationInterface."""
        super().__init__()
        self.attributes: list[Field] = []
        self.commands: list[ClientServerOperation] = []
        self.indication_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationInterface":
        """Deserialize XML element to ApplicationInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationInterface object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse attributes (list)
        obj.attributes = []
        for child in ARObject._find_all_child_elements(element, "ATTRIBUTES"):
            attributes_value = ARObject._deserialize_by_tag(child, "Field")
            obj.attributes.append(attributes_value)

        # Parse commands (list)
        obj.commands = []
        for child in ARObject._find_all_child_elements(element, "COMMANDS"):
            commands_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.commands.append(commands_value)

        # Parse indication_refs (list)
        obj.indication_refs = []
        for child in ARObject._find_all_child_elements(element, "INDICATIONS"):
            indication_refs_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.indication_refs.append(indication_refs_value)

        return obj



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
