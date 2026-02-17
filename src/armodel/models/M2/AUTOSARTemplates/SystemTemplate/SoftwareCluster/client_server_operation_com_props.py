"""ClientServerOperationComProps AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ClientServerOperationComProps(CpSoftwareClusterCommunicationResourceProps):
    """AUTOSAR ClientServerOperationComProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize ClientServerOperationComProps."""
        super().__init__()


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
