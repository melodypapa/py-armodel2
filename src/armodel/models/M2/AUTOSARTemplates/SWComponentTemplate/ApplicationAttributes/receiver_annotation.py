"""ReceiverAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.sender_receiver_annotation import (
    SenderReceiverAnnotation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ReceiverAnnotation(SenderReceiverAnnotation):
    """AUTOSAR ReceiverAnnotation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    signal_age: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize ReceiverAnnotation."""
        super().__init__()
        self.signal_age: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize ReceiverAnnotation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReceiverAnnotation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize signal_age
        if self.signal_age is not None:
            serialized = SerializationHelper.serialize_item(self.signal_age, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-AGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceiverAnnotation":
        """Deserialize XML element to ReceiverAnnotation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReceiverAnnotation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReceiverAnnotation, cls).deserialize(element)

        # Parse signal_age
        child = SerializationHelper.find_child_element(element, "SIGNAL-AGE")
        if child is not None:
            signal_age_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.signal_age = signal_age_value

        return obj



class ReceiverAnnotationBuilder:
    """Builder for ReceiverAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceiverAnnotation = ReceiverAnnotation()

    def build(self) -> ReceiverAnnotation:
        """Build and return ReceiverAnnotation object.

        Returns:
            ReceiverAnnotation instance
        """
        # TODO: Add validation
        return self._obj
