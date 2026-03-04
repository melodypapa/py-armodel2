"""ISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ISignalProps(ARObject):
    """AUTOSAR ISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-SIGNAL-PROPS"


    handle_out_of_range: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "HANDLE-OUT-OF-RANGE": lambda obj, elem: setattr(obj, "handle_out_of_range", SerializationHelper.deserialize_by_tag(elem, "any (HandleOutOfRange)")),
    }


    def __init__(self) -> None:
        """Initialize ISignalProps."""
        super().__init__()
        self.handle_out_of_range: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize handle_out_of_range
        if self.handle_out_of_range is not None:
            serialized = SerializationHelper.serialize_item(self.handle_out_of_range, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-OUT-OF-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalProps":
        """Deserialize XML element to ISignalProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HANDLE-OUT-OF-RANGE":
                setattr(obj, "handle_out_of_range", SerializationHelper.deserialize_by_tag(child, "any (HandleOutOfRange)"))

        return obj



class ISignalPropsBuilder(BuilderBase):
    """Builder for ISignalProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignalProps = ISignalProps()


    def with_handle_out_of_range(self, value: Optional[any (HandleOutOfRange)]) -> "ISignalPropsBuilder":
        """Set handle_out_of_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_out_of_range = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "handleOutOfRange",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ISignalProps:
        """Build and return the ISignalProps instance with validation."""
        self._validate_instance()
        return self._obj