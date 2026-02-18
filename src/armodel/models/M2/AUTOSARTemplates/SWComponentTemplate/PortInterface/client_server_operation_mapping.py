"""ClientServerOperationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    arguments: list[DataPrototypeMapping]
    first_operation: Optional[ClientServerOperation]
    first_to_second: Optional[DataTransformation]
    second: Optional[ClientServerOperation]
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
