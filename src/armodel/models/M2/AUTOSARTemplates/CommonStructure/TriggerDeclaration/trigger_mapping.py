"""TriggerMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 134)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_TriggerDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerMapping(ARObject):
    """AUTOSAR TriggerMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_trigger_ref: Optional[ARRef]
    second_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TriggerMapping."""
        super().__init__()
        self.first_trigger_ref: Optional[ARRef] = None
        self.second_trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TriggerMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TriggerMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_trigger_ref
        if self.first_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_trigger_ref
        if self.second_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerMapping":
        """Deserialize XML element to TriggerMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TriggerMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TriggerMapping, cls).deserialize(element)

        # Parse first_trigger_ref
        child = SerializationHelper.find_child_element(element, "FIRST-TRIGGER-REF")
        if child is not None:
            first_trigger_ref_value = ARRef.deserialize(child)
            obj.first_trigger_ref = first_trigger_ref_value

        # Parse second_trigger_ref
        child = SerializationHelper.find_child_element(element, "SECOND-TRIGGER-REF")
        if child is not None:
            second_trigger_ref_value = ARRef.deserialize(child)
            obj.second_trigger_ref = second_trigger_ref_value

        return obj



class TriggerMappingBuilder:
    """Builder for TriggerMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerMapping = TriggerMapping()

    def build(self) -> TriggerMapping:
        """Build and return TriggerMapping object.

        Returns:
            TriggerMapping instance
        """
        # TODO: Add validation
        return self._obj
