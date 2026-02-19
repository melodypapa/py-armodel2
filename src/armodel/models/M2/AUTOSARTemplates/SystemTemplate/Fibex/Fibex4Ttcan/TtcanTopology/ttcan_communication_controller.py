"""TtcanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


class TtcanCommunicationController(ARObject):
    """AUTOSAR TtcanCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    appl_watchdog: Optional[Integer]
    expected_tx: Optional[Integer]
    external_clock: Optional[Boolean]
    initial_ref_offset: Optional[Integer]
    master: Optional[Boolean]
    time_master: Optional[Integer]
    time_triggered: Optional[Integer]
    tx_enable: Optional[Integer]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanCommunicationController":
        """Deserialize XML element to TtcanCommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse appl_watchdog
        child = ARObject._find_child_element(element, "APPL-WATCHDOG")
        if child is not None:
            appl_watchdog_value = child.text
            obj.appl_watchdog = appl_watchdog_value

        # Parse expected_tx
        child = ARObject._find_child_element(element, "EXPECTED-TX")
        if child is not None:
            expected_tx_value = child.text
            obj.expected_tx = expected_tx_value

        # Parse external_clock
        child = ARObject._find_child_element(element, "EXTERNAL-CLOCK")
        if child is not None:
            external_clock_value = child.text
            obj.external_clock = external_clock_value

        # Parse initial_ref_offset
        child = ARObject._find_child_element(element, "INITIAL-REF-OFFSET")
        if child is not None:
            initial_ref_offset_value = child.text
            obj.initial_ref_offset = initial_ref_offset_value

        # Parse master
        child = ARObject._find_child_element(element, "MASTER")
        if child is not None:
            master_value = child.text
            obj.master = master_value

        # Parse time_master
        child = ARObject._find_child_element(element, "TIME-MASTER")
        if child is not None:
            time_master_value = child.text
            obj.time_master = time_master_value

        # Parse time_triggered
        child = ARObject._find_child_element(element, "TIME-TRIGGERED")
        if child is not None:
            time_triggered_value = child.text
            obj.time_triggered = time_triggered_value

        # Parse tx_enable
        child = ARObject._find_child_element(element, "TX-ENABLE")
        if child is not None:
            tx_enable_value = child.text
            obj.tx_enable = tx_enable_value

        return obj



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
