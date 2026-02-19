"""ClientServerOperationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    argument_refs: list[ARRef]
    first_operation: Optional[ClientServerOperation]
    first_to_second: Optional[DataTransformation]
    second: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize ClientServerOperationMapping."""
        super().__init__()
        self.argument_refs: list[ARRef] = []
        self.first_operation: Optional[ClientServerOperation] = None
        self.first_to_second: Optional[DataTransformation] = None
        self.second: Optional[ClientServerOperation] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationMapping":
        """Deserialize XML element to ClientServerOperationMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperationMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse argument_refs (list)
        obj.argument_refs = []
        for child in ARObject._find_all_child_elements(element, "ARGUMENTS"):
            argument_refs_value = ARObject._deserialize_by_tag(child, "DataPrototypeMapping")
            obj.argument_refs.append(argument_refs_value)

        # Parse first_operation
        child = ARObject._find_child_element(element, "FIRST-OPERATION")
        if child is not None:
            first_operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.first_operation = first_operation_value

        # Parse first_to_second
        child = ARObject._find_child_element(element, "FIRST-TO-SECOND")
        if child is not None:
            first_to_second_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.first_to_second = first_to_second_value

        # Parse second
        child = ARObject._find_child_element(element, "SECOND")
        if child is not None:
            second_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.second = second_value

        return obj



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
