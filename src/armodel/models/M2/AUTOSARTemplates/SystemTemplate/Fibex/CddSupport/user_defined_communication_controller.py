"""UserDefinedCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_CddSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedCommunicationController(ARObject):
    """AUTOSAR UserDefinedCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UserDefinedCommunicationController."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize UserDefinedCommunicationController to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedCommunicationController":
        """Deserialize XML element to UserDefinedCommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class UserDefinedCommunicationControllerBuilder:
    """Builder for UserDefinedCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedCommunicationController = UserDefinedCommunicationController()

    def build(self) -> UserDefinedCommunicationController:
        """Build and return UserDefinedCommunicationController object.

        Returns:
            UserDefinedCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
