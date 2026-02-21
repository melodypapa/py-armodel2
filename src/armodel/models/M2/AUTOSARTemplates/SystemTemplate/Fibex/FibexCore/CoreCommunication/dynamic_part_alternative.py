"""DynamicPartAlternative AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class DynamicPartAlternative(ARObject):
    """AUTOSAR DynamicPartAlternative."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_dynamic: Optional[Boolean]
    i_pdu_ref: Optional[ARRef]
    selector_field: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DynamicPartAlternative."""
        super().__init__()
        self.initial_dynamic: Optional[Boolean] = None
        self.i_pdu_ref: Optional[ARRef] = None
        self.selector_field: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize DynamicPartAlternative to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DynamicPartAlternative, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_dynamic
        if self.initial_dynamic is not None:
            serialized = SerializationHelper.serialize_item(self.initial_dynamic, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-DYNAMIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_ref
        if self.i_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_ref, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize selector_field
        if self.selector_field is not None:
            serialized = SerializationHelper.serialize_item(self.selector_field, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SELECTOR-FIELD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DynamicPartAlternative":
        """Deserialize XML element to DynamicPartAlternative object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DynamicPartAlternative object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DynamicPartAlternative, cls).deserialize(element)

        # Parse initial_dynamic
        child = SerializationHelper.find_child_element(element, "INITIAL-DYNAMIC")
        if child is not None:
            initial_dynamic_value = child.text
            obj.initial_dynamic = initial_dynamic_value

        # Parse i_pdu_ref
        child = SerializationHelper.find_child_element(element, "I-PDU-REF")
        if child is not None:
            i_pdu_ref_value = ARRef.deserialize(child)
            obj.i_pdu_ref = i_pdu_ref_value

        # Parse selector_field
        child = SerializationHelper.find_child_element(element, "SELECTOR-FIELD")
        if child is not None:
            selector_field_value = child.text
            obj.selector_field = selector_field_value

        return obj



class DynamicPartAlternativeBuilder:
    """Builder for DynamicPartAlternative."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DynamicPartAlternative = DynamicPartAlternative()

    def build(self) -> DynamicPartAlternative:
        """Build and return DynamicPartAlternative object.

        Returns:
            DynamicPartAlternative instance
        """
        # TODO: Add validation
        return self._obj
