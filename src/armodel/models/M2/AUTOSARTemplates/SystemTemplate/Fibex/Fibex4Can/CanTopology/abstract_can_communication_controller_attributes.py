"""AbstractCanCommunicationControllerAttributes AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class AbstractCanCommunicationControllerAttributes(ARObject, ABC):
    """AUTOSAR AbstractCanCommunicationControllerAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    can_controller_fd: Optional[Any]
    can_controller_xl: Optional[Any]
    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationControllerAttributes."""
        super().__init__()
        self.can_controller_fd: Optional[Any] = None
        self.can_controller_xl: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractCanCommunicationControllerAttributes to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize can_controller_fd
        if self.can_controller_fd is not None:
            serialized = SerializationHelper.serialize_item(self.can_controller_fd, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-CONTROLLER-FD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_controller_xl
        if self.can_controller_xl is not None:
            serialized = SerializationHelper.serialize_item(self.can_controller_xl, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-CONTROLLER-XL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationControllerAttributes":
        """Deserialize XML element to AbstractCanCommunicationControllerAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCommunicationControllerAttributes object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse can_controller_fd
        child = SerializationHelper.find_child_element(element, "CAN-CONTROLLER-FD")
        if child is not None:
            can_controller_fd_value = child.text
            obj.can_controller_fd = can_controller_fd_value

        # Parse can_controller_xl
        child = SerializationHelper.find_child_element(element, "CAN-CONTROLLER-XL")
        if child is not None:
            can_controller_xl_value = child.text
            obj.can_controller_xl = can_controller_xl_value

        return obj



class AbstractCanCommunicationControllerAttributesBuilder:
    """Builder for AbstractCanCommunicationControllerAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationControllerAttributes = AbstractCanCommunicationControllerAttributes()

    def build(self) -> AbstractCanCommunicationControllerAttributes:
        """Build and return AbstractCanCommunicationControllerAttributes object.

        Returns:
            AbstractCanCommunicationControllerAttributes instance
        """
        # TODO: Add validation
        return self._obj
