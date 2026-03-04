"""J1939DcmIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import IPduBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939DcmIPdu(IPdu):
    """AUTOSAR J1939DcmIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-DCM-I-PDU"


    diagnostic: Optional[PositiveInteger]
    message_type: Any
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTIC": lambda obj, elem: setattr(obj, "diagnostic", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MESSAGE-TYPE": lambda obj, elem: setattr(obj, "message_type", SerializationHelper.deserialize_by_tag(elem, "any (e.g)")),
    }


    def __init__(self) -> None:
        """Initialize J1939DcmIPdu."""
        super().__init__()
        self.diagnostic: Optional[PositiveInteger] = None
        self.message_type: Any = None

    def serialize(self) -> ET.Element:
        """Serialize J1939DcmIPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939DcmIPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic
        if self.diagnostic is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize message_type
        if self.message_type is not None:
            serialized = SerializationHelper.serialize_item(self.message_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939DcmIPdu":
        """Deserialize XML element to J1939DcmIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939DcmIPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939DcmIPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAGNOSTIC":
                setattr(obj, "diagnostic", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MESSAGE-TYPE":
                setattr(obj, "message_type", SerializationHelper.deserialize_by_tag(child, "any (e.g)"))

        return obj



class J1939DcmIPduBuilder(IPduBuilder):
    """Builder for J1939DcmIPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939DcmIPdu = J1939DcmIPdu()


    def with_diagnostic(self, value: Optional[PositiveInteger]) -> "J1939DcmIPduBuilder":
        """Set diagnostic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic = value
        return self

    def with_message_type(self, value: any (e.g)) -> "J1939DcmIPduBuilder":
        """Set message_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.message_type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "MessageType",
    }
    _OPTIONAL_ATTRIBUTES = {
        "diagnostic",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "MessageType", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'MessageType' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'MessageType' is None", UserWarning)


    def build(self) -> J1939DcmIPdu:
        """Build and return the J1939DcmIPdu instance with validation."""
        self._validate_instance()
        return self._obj