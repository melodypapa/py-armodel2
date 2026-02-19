"""UserDefinedCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_CddSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedCommunicationConnector(CommunicationConnector):
    """AUTOSAR UserDefinedCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UserDefinedCommunicationConnector."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedCommunicationConnector":
        """Deserialize XML element to UserDefinedCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedCommunicationConnector object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class UserDefinedCommunicationConnectorBuilder:
    """Builder for UserDefinedCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedCommunicationConnector = UserDefinedCommunicationConnector()

    def build(self) -> UserDefinedCommunicationConnector:
        """Build and return UserDefinedCommunicationConnector object.

        Returns:
            UserDefinedCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
