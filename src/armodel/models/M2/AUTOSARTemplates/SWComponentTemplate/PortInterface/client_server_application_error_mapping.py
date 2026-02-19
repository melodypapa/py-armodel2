"""ClientServerApplicationErrorMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)


class ClientServerApplicationErrorMapping(ARObject):
    """AUTOSAR ClientServerApplicationErrorMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_application: Optional[ApplicationError]
    second: Optional[ApplicationError]
    def __init__(self) -> None:
        """Initialize ClientServerApplicationErrorMapping."""
        super().__init__()
        self.first_application: Optional[ApplicationError] = None
        self.second: Optional[ApplicationError] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerApplicationErrorMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize first_application
        if self.first_application is not None:
            serialized = ARObject._serialize_item(self.first_application, "ApplicationError")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-APPLICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second
        if self.second is not None:
            serialized = ARObject._serialize_item(self.second, "ApplicationError")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerApplicationErrorMapping":
        """Deserialize XML element to ClientServerApplicationErrorMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerApplicationErrorMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse first_application
        child = ARObject._find_child_element(element, "FIRST-APPLICATION")
        if child is not None:
            first_application_value = ARObject._deserialize_by_tag(child, "ApplicationError")
            obj.first_application = first_application_value

        # Parse second
        child = ARObject._find_child_element(element, "SECOND")
        if child is not None:
            second_value = ARObject._deserialize_by_tag(child, "ApplicationError")
            obj.second = second_value

        return obj



class ClientServerApplicationErrorMappingBuilder:
    """Builder for ClientServerApplicationErrorMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerApplicationErrorMapping = ClientServerApplicationErrorMapping()

    def build(self) -> ClientServerApplicationErrorMapping:
        """Build and return ClientServerApplicationErrorMapping object.

        Returns:
            ClientServerApplicationErrorMapping instance
        """
        # TODO: Add validation
        return self._obj
