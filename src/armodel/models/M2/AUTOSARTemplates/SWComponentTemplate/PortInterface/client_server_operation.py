"""ClientServerOperation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 309)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 306)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 102)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2008)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 218)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 28)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 433)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    argument_refs: list[ARRef]
    diag_arg_integrity: Optional[Boolean]
    possible_errors: list[ApplicationError]
    def __init__(self) -> None:
        """Initialize ClientServerOperation."""
        super().__init__()
        self.argument_refs: list[ARRef] = []
        self.diag_arg_integrity: Optional[Boolean] = None
        self.possible_errors: list[ApplicationError] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperation":
        """Deserialize XML element to ClientServerOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse argument_refs (list)
        obj.argument_refs = []
        for child in ARObject._find_all_child_elements(element, "ARGUMENTS"):
            argument_refs_value = ARObject._deserialize_by_tag(child, "ArgumentDataPrototype")
            obj.argument_refs.append(argument_refs_value)

        # Parse diag_arg_integrity
        child = ARObject._find_child_element(element, "DIAG-ARG-INTEGRITY")
        if child is not None:
            diag_arg_integrity_value = child.text
            obj.diag_arg_integrity = diag_arg_integrity_value

        # Parse possible_errors (list)
        obj.possible_errors = []
        for child in ARObject._find_all_child_elements(element, "POSSIBLE-ERRORS"):
            possible_errors_value = ARObject._deserialize_by_tag(child, "ApplicationError")
            obj.possible_errors.append(possible_errors_value)

        return obj



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
