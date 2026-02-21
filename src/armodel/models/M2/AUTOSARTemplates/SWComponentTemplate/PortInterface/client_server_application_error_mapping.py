"""ClientServerApplicationErrorMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    first_application_ref: Optional[ARRef]
    second_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ClientServerApplicationErrorMapping."""
        super().__init__()
        self.first_application_ref: Optional[ARRef] = None
        self.second_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerApplicationErrorMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerApplicationErrorMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_application_ref
        if self.first_application_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_application_ref, "ApplicationError")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-APPLICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_ref
        if self.second_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_ref, "ApplicationError")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerApplicationErrorMapping, cls).deserialize(element)

        # Parse first_application_ref
        child = SerializationHelper.find_child_element(element, "FIRST-APPLICATION-REF")
        if child is not None:
            first_application_ref_value = ARRef.deserialize(child)
            obj.first_application_ref = first_application_ref_value

        # Parse second_ref
        child = SerializationHelper.find_child_element(element, "SECOND-REF")
        if child is not None:
            second_ref_value = ARRef.deserialize(child)
            obj.second_ref = second_ref_value

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
