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
from armodel.serialization import SerializationHelper


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

    def serialize(self) -> ET.Element:
        """Serialize UserDefinedCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UserDefinedCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedCommunicationConnector":
        """Deserialize XML element to UserDefinedCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedCommunicationConnector object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedCommunicationConnector, cls).deserialize(element)



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
