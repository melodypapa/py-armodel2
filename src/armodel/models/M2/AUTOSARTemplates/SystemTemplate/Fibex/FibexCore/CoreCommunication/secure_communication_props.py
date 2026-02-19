"""SecureCommunicationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecureCommunicationProps(ARObject):
    """AUTOSAR SecureCommunicationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auth_data: Optional[PositiveInteger]
    authentication: Optional[PositiveInteger]
    data_id: Optional[PositiveInteger]
    freshness_value: Optional[PositiveInteger]
    message_link: Optional[PositiveInteger]
    secondary: Optional[PositiveInteger]
    secured_area: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecureCommunicationProps."""
        super().__init__()
        self.auth_data: Optional[PositiveInteger] = None
        self.authentication: Optional[PositiveInteger] = None
        self.data_id: Optional[PositiveInteger] = None
        self.freshness_value: Optional[PositiveInteger] = None
        self.message_link: Optional[PositiveInteger] = None
        self.secondary: Optional[PositiveInteger] = None
        self.secured_area: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationProps":
        """Deserialize XML element to SecureCommunicationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecureCommunicationProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse auth_data
        child = ARObject._find_child_element(element, "AUTH-DATA")
        if child is not None:
            auth_data_value = child.text
            obj.auth_data = auth_data_value

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = child.text
            obj.authentication = authentication_value

        # Parse data_id
        child = ARObject._find_child_element(element, "DATA-ID")
        if child is not None:
            data_id_value = child.text
            obj.data_id = data_id_value

        # Parse freshness_value
        child = ARObject._find_child_element(element, "FRESHNESS-VALUE")
        if child is not None:
            freshness_value_value = child.text
            obj.freshness_value = freshness_value_value

        # Parse message_link
        child = ARObject._find_child_element(element, "MESSAGE-LINK")
        if child is not None:
            message_link_value = child.text
            obj.message_link = message_link_value

        # Parse secondary
        child = ARObject._find_child_element(element, "SECONDARY")
        if child is not None:
            secondary_value = child.text
            obj.secondary = secondary_value

        # Parse secured_area
        child = ARObject._find_child_element(element, "SECURED-AREA")
        if child is not None:
            secured_area_value = child.text
            obj.secured_area = secured_area_value

        return obj



class SecureCommunicationPropsBuilder:
    """Builder for SecureCommunicationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationProps = SecureCommunicationProps()

    def build(self) -> SecureCommunicationProps:
        """Build and return SecureCommunicationProps object.

        Returns:
            SecureCommunicationProps instance
        """
        # TODO: Add validation
        return self._obj
