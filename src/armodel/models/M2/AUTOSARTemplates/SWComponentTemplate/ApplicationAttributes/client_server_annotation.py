"""ClientServerAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 155)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation.general_annotation import (
    GeneralAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerAnnotation(GeneralAnnotation):
    """AUTOSAR ClientServerAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize ClientServerAnnotation."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerAnnotation":
        """Deserialize XML element to ClientServerAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerAnnotation, cls).deserialize(element)

        # Parse operation
        child = ARObject._find_child_element(element, "OPERATION")
        if child is not None:
            operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation = operation_value

        return obj



class ClientServerAnnotationBuilder:
    """Builder for ClientServerAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerAnnotation = ClientServerAnnotation()

    def build(self) -> ClientServerAnnotation:
        """Build and return ClientServerAnnotation object.

        Returns:
            ClientServerAnnotation instance
        """
        # TODO: Add validation
        return self._obj
