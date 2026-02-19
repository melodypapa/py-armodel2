"""CommunicationBufferLocking AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 595)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import (
    SupportBufferLockingEnum,
)


class CommunicationBufferLocking(SwcSupportedFeature):
    """AUTOSAR CommunicationBufferLocking."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    support_buffer_locking: Optional[SupportBufferLockingEnum]
    def __init__(self) -> None:
        """Initialize CommunicationBufferLocking."""
        super().__init__()
        self.support_buffer_locking: Optional[SupportBufferLockingEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationBufferLocking":
        """Deserialize XML element to CommunicationBufferLocking object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationBufferLocking object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse support_buffer_locking
        child = ARObject._find_child_element(element, "SUPPORT-BUFFER-LOCKING")
        if child is not None:
            support_buffer_locking_value = child.text
            obj.support_buffer_locking = support_buffer_locking_value

        return obj



class CommunicationBufferLockingBuilder:
    """Builder for CommunicationBufferLocking."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationBufferLocking = CommunicationBufferLocking()

    def build(self) -> CommunicationBufferLocking:
        """Build and return CommunicationBufferLocking object.

        Returns:
            CommunicationBufferLocking instance
        """
        # TODO: Add validation
        return self._obj
