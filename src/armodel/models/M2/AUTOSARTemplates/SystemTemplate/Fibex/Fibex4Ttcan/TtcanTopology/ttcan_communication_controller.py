"""TtcanCommunicationController AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


class TtcanCommunicationController(ARObject):
    """AUTOSAR TtcanCommunicationController."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("appl_watchdog", None, True, False, None),  # applWatchdog
        ("expected_tx", None, True, False, None),  # expectedTx
        ("external_clock", None, True, False, None),  # externalClock
        ("initial_ref_offset", None, True, False, None),  # initialRefOffset
        ("master", None, True, False, None),  # master
        ("time_master", None, True, False, None),  # timeMaster
        ("time_triggered", None, True, False, None),  # timeTriggered
        ("tx_enable", None, True, False, None),  # txEnable
    ]

    def __init__(self) -> None:
        """Initialize TtcanCommunicationController."""
        super().__init__()
        self.appl_watchdog: Optional[Integer] = None
        self.expected_tx: Optional[Integer] = None
        self.external_clock: Optional[Boolean] = None
        self.initial_ref_offset: Optional[Integer] = None
        self.master: Optional[Boolean] = None
        self.time_master: Optional[Integer] = None
        self.time_triggered: Optional[Integer] = None
        self.tx_enable: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TtcanCommunicationController to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanCommunicationController":
        """Create TtcanCommunicationController from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TtcanCommunicationController instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TtcanCommunicationController since parent returns ARObject
        return cast("TtcanCommunicationController", obj)


class TtcanCommunicationControllerBuilder:
    """Builder for TtcanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanCommunicationController = TtcanCommunicationController()

    def build(self) -> TtcanCommunicationController:
        """Build and return TtcanCommunicationController object.

        Returns:
            TtcanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
