"""UserDefinedPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_CddSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedPhysicalChannel(PhysicalChannel):
    """AUTOSAR UserDefinedPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UserDefinedPhysicalChannel."""
        super().__init__()
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedPhysicalChannel":
        """Deserialize XML element to UserDefinedPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedPhysicalChannel object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedPhysicalChannel, cls).deserialize(element)



class UserDefinedPhysicalChannelBuilder:
    """Builder for UserDefinedPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedPhysicalChannel = UserDefinedPhysicalChannel()

    def build(self) -> UserDefinedPhysicalChannel:
        """Build and return UserDefinedPhysicalChannel object.

        Returns:
            UserDefinedPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
