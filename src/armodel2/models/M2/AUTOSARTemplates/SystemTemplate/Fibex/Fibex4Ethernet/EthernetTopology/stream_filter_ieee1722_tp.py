"""StreamFilterIEEE1722Tp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class StreamFilterIEEE1722Tp(ARObject):
    """AUTOSAR StreamFilterIEEE1722Tp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STREAM-FILTER-I-E-E-E1722-TP"


    stream_id: Optional[PositiveUnlimitedInteger]
    _DESERIALIZE_DISPATCH = {
        "STREAM-ID": lambda obj, elem: setattr(obj, "stream_id", SerializationHelper.deserialize_by_tag(elem, "PositiveUnlimitedInteger")),
    }


    def __init__(self) -> None:
        """Initialize StreamFilterIEEE1722Tp."""
        super().__init__()
        self.stream_id: Optional[PositiveUnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterIEEE1722Tp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StreamFilterIEEE1722Tp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize stream_id
        if self.stream_id is not None:
            serialized = SerializationHelper.serialize_item(self.stream_id, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterIEEE1722Tp":
        """Deserialize XML element to StreamFilterIEEE1722Tp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterIEEE1722Tp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StreamFilterIEEE1722Tp, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "STREAM-ID":
                setattr(obj, "stream_id", SerializationHelper.deserialize_by_tag(child, "PositiveUnlimitedInteger"))

        return obj



class StreamFilterIEEE1722TpBuilder(BuilderBase):
    """Builder for StreamFilterIEEE1722Tp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StreamFilterIEEE1722Tp = StreamFilterIEEE1722Tp()


    def with_stream_id(self, value: Optional[PositiveUnlimitedInteger]) -> "StreamFilterIEEE1722TpBuilder":
        """Set stream_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'stream_id' is required and cannot be None")
        self._obj.stream_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "streamId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> StreamFilterIEEE1722Tp:
        """Build and return the StreamFilterIEEE1722Tp instance with validation."""
        self._validate_instance()
        return self._obj