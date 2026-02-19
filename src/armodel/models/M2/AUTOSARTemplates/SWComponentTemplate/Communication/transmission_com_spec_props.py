"""TransmissionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2075)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TransmissionComSpecProps(ARObject):
    """AUTOSAR TransmissionComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_update: Optional[TimeValue]
    minimum_send: Optional[TimeValue]
    transmission: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransmissionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.minimum_send: Optional[TimeValue] = None
        self.transmission: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionComSpecProps":
        """Deserialize XML element to TransmissionComSpecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionComSpecProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_update
        child = ARObject._find_child_element(element, "DATA-UPDATE")
        if child is not None:
            data_update_value = child.text
            obj.data_update = data_update_value

        # Parse minimum_send
        child = ARObject._find_child_element(element, "MINIMUM-SEND")
        if child is not None:
            minimum_send_value = child.text
            obj.minimum_send = minimum_send_value

        # Parse transmission
        child = ARObject._find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class TransmissionComSpecPropsBuilder:
    """Builder for TransmissionComSpecProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionComSpecProps = TransmissionComSpecProps()

    def build(self) -> TransmissionComSpecProps:
        """Build and return TransmissionComSpecProps object.

        Returns:
            TransmissionComSpecProps instance
        """
        # TODO: Add validation
        return self._obj
