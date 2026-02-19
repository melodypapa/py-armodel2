"""AbstractCanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractCanCommunicationController(ARObject, ABC):
    """AUTOSAR AbstractCanCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    can_controller_controller_attributes: Optional[Any]
    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationController."""
        super().__init__()
        self.can_controller_controller_attributes: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize AbstractCanCommunicationController to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize can_controller_controller_attributes
        if self.can_controller_controller_attributes is not None:
            serialized = ARObject._serialize_item(self.can_controller_controller_attributes, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-CONTROLLER-CONTROLLER-ATTRIBUTES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationController":
        """Deserialize XML element to AbstractCanCommunicationController object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse can_controller_controller_attributes
        child = ARObject._find_child_element(element, "CAN-CONTROLLER-CONTROLLER-ATTRIBUTES")
        if child is not None:
            can_controller_controller_attributes_value = child.text
            obj.can_controller_controller_attributes = can_controller_controller_attributes_value

        return obj



class AbstractCanCommunicationControllerBuilder:
    """Builder for AbstractCanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationController = AbstractCanCommunicationController()

    def build(self) -> AbstractCanCommunicationController:
        """Build and return AbstractCanCommunicationController object.

        Returns:
            AbstractCanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
