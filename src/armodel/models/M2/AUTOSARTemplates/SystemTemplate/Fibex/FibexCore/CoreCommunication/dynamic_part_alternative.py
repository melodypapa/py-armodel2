"""DynamicPartAlternative AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    i_pdu: Optional[ISignalIPdu]
    selector_field: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DynamicPartAlternative."""
        super().__init__()
        self.initial_dynamic: Optional[Boolean] = None
        self.i_pdu: Optional[ISignalIPdu] = None
        self.selector_field: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize DynamicPartAlternative to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize initial_dynamic
        if self.initial_dynamic is not None:
            serialized = ARObject._serialize_item(self.initial_dynamic, "Boolean")
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

        # Serialize i_pdu
        if self.i_pdu is not None:
            serialized = ARObject._serialize_item(self.i_pdu, "ISignalIPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize selector_field
        if self.selector_field is not None:
            serialized = ARObject._serialize_item(self.selector_field, "Integer")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse initial_dynamic
        child = ARObject._find_child_element(element, "INITIAL-DYNAMIC")
        if child is not None:
            initial_dynamic_value = child.text
            obj.initial_dynamic = initial_dynamic_value

        # Parse i_pdu
        child = ARObject._find_child_element(element, "I-PDU")
        if child is not None:
            i_pdu_value = ARObject._deserialize_by_tag(child, "ISignalIPdu")
            obj.i_pdu = i_pdu_value

        # Parse selector_field
        child = ARObject._find_child_element(element, "SELECTOR-FIELD")
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
