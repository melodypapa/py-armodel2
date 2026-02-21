"""CommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class CommunicationController(ARObject, ABC):
    """AUTOSAR CommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    wake_up_by: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CommunicationController."""
        super().__init__()
        self.wake_up_by: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationController, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize wake_up_by
        if self.wake_up_by is not None:
            serialized = SerializationHelper.serialize_item(self.wake_up_by, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("WAKE-UP-BY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "CommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationController":
        """Deserialize XML element to CommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationController object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationController, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "CommunicationController")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse wake_up_by
        child = SerializationHelper.find_child_element(inner_elem, "WAKE-UP-BY")
        if child is not None:
            wake_up_by_value = child.text
            obj.wake_up_by = wake_up_by_value

        return obj



class CommunicationControllerBuilder:
    """Builder for CommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationController = CommunicationController()

    def build(self) -> CommunicationController:
        """Build and return CommunicationController object.

        Returns:
            CommunicationController instance
        """
        # TODO: Add validation
        return self._obj
