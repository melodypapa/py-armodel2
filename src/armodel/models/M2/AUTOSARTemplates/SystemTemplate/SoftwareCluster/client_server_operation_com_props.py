"""ClientServerOperationComProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_communication_resource_props import (
    CpSoftwareClusterCommunicationResourceProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR ClientServerOperationComProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    queue_length: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ClientServerOperationComProps."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationComProps":
        """Deserialize XML element to ClientServerOperationComProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperationComProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerOperationComProps, cls).deserialize(element)

        # Parse queue_length
        child = ARObject._find_child_element(element, "QUEUE-LENGTH")
        if child is not None:
            queue_length_value = child.text
            obj.queue_length = queue_length_value

        return obj



class ClientServerOperationComPropsBuilder:
    """Builder for ClientServerOperationComProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationComProps = ClientServerOperationComProps()

    def build(self) -> ClientServerOperationComProps:
        """Build and return ClientServerOperationComProps object.

        Returns:
            ClientServerOperationComProps instance
        """
        # TODO: Add validation
        return self._obj
