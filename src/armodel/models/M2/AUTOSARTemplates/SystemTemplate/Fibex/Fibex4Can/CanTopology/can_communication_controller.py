"""CanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanCommunicationController(ARObject):
    """AUTOSAR CanCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanCommunicationController."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize CanCommunicationController to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanCommunicationController":
        """Deserialize XML element to CanCommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class CanCommunicationControllerBuilder:
    """Builder for CanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanCommunicationController = CanCommunicationController()

    def build(self) -> CanCommunicationController:
        """Build and return CanCommunicationController object.

        Returns:
            CanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
