"""LinErrorResponse AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 97)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinErrorResponse(ARObject):
    """AUTOSAR LinErrorResponse."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-ERROR-RESPONSE"


    response_error_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "RESPONSE-ERROR-REF": lambda obj, elem: setattr(obj, "response_error_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize LinErrorResponse."""
        super().__init__()
        self.response_error_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize LinErrorResponse to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinErrorResponse, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize response_error_ref
        if self.response_error_ref is not None:
            serialized = SerializationHelper.serialize_item(self.response_error_ref, "ISignalTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ERROR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinErrorResponse":
        """Deserialize XML element to LinErrorResponse object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinErrorResponse object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinErrorResponse, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RESPONSE-ERROR-REF":
                setattr(obj, "response_error_ref", ARRef.deserialize(child))

        return obj



class LinErrorResponseBuilder(BuilderBase):
    """Builder for LinErrorResponse with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinErrorResponse = LinErrorResponse()


    def with_response_error(self, value: Optional[ISignalTriggering]) -> "LinErrorResponseBuilder":
        """Set response_error attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_error = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "responseError",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinErrorResponse:
        """Build and return the LinErrorResponse instance with validation."""
        self._validate_instance()
        return self._obj