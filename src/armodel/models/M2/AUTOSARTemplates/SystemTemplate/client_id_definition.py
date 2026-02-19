"""ClientIdDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 45)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientIdDefinition(Identifiable):
    """AUTOSAR ClientIdDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_id: Optional[Numerical]
    client_server_instance_ref: Optional[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize ClientIdDefinition."""
        super().__init__()
        self.client_id: Optional[Numerical] = None
        self.client_server_instance_ref: Optional[ClientServerOperation] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdDefinition":
        """Deserialize XML element to ClientIdDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientIdDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientIdDefinition, cls).deserialize(element)

        # Parse client_id
        child = ARObject._find_child_element(element, "CLIENT-ID")
        if child is not None:
            client_id_value = child.text
            obj.client_id = client_id_value

        # Parse client_server_instance_ref
        child = ARObject._find_child_element(element, "CLIENT-SERVER-INSTANCE-REF")
        if child is not None:
            client_server_instance_ref_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.client_server_instance_ref = client_server_instance_ref_value

        return obj



class ClientIdDefinitionBuilder:
    """Builder for ClientIdDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdDefinition = ClientIdDefinition()

    def build(self) -> ClientIdDefinition:
        """Build and return ClientIdDefinition object.

        Returns:
            ClientIdDefinition instance
        """
        # TODO: Add validation
        return self._obj
