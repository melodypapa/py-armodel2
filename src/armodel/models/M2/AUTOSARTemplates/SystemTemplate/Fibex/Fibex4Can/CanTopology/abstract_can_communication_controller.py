"""AbstractCanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
        """Serialize AbstractCanCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize can_controller_controller_attributes
        if self.can_controller_controller_attributes is not None:
            serialized = SerializationHelper.serialize_item(self.can_controller_controller_attributes, "Any")
            if serialized is not None:
                wrapped = ET.Element("CAN-CONTROLLER-CONTROLLER-ATTRIBUTES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "AbstractCanCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationController":
        """Deserialize XML element to AbstractCanCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Handle ARObject inherited attributes (checksum and timestamp)
        # Parse timestamp (XML attribute 'T')
        timestamp_value = element.get("T")
        if timestamp_value is not None:
            obj.timestamp = timestamp_value

        # Parse checksum (child element)
        checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
        if checksum_elem is not None:
            checksum_value = checksum_elem.text
            if checksum_value is not None:
                obj.checksum = checksum_value

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "AbstractCanCommunicationController")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse can_controller_controller_attributes
        child = SerializationHelper.find_child_element(inner_elem, "CAN-CONTROLLER-CONTROLLER-ATTRIBUTES")
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
