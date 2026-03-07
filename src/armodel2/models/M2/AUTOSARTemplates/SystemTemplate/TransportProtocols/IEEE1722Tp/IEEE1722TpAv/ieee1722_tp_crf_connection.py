"""IEEE1722TpCrfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 640)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import IEEE1722TpAvConnectionBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpCrfPullEnum,
    IEEE1722TpCrfTypeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpCrfConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-CRF-CONNECTION"


    base_frequency: Optional[PositiveInteger]
    crf_pull_enum: Optional[IEEE1722TpCrfPullEnum]
    crf_type_enum: Optional[IEEE1722TpCrfTypeEnum]
    frame_sync: Optional[Boolean]
    timestamp: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "BASE-FREQUENCY": lambda obj, elem: setattr(obj, "base_frequency", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "CRF-PULL-ENUM": lambda obj, elem: setattr(obj, "crf_pull_enum", IEEE1722TpCrfPullEnum.deserialize(elem)),
        "CRF-TYPE-ENUM": lambda obj, elem: setattr(obj, "crf_type_enum", IEEE1722TpCrfTypeEnum.deserialize(elem)),
        "FRAME-SYNC": lambda obj, elem: setattr(obj, "frame_sync", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TIMESTAMP": lambda obj, elem: setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpCrfConnection."""
        super().__init__()
        self.base_frequency: Optional[PositiveInteger] = None
        self.crf_pull_enum: Optional[IEEE1722TpCrfPullEnum] = None
        self.crf_type_enum: Optional[IEEE1722TpCrfTypeEnum] = None
        self.frame_sync: Optional[Boolean] = None
        self.timestamp: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpCrfConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpCrfConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_frequency
        if self.base_frequency is not None:
            serialized = SerializationHelper.serialize_item(self.base_frequency, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-FREQUENCY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crf_pull_enum
        if self.crf_pull_enum is not None:
            serialized = SerializationHelper.serialize_item(self.crf_pull_enum, "IEEE1722TpCrfPullEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRF-PULL-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crf_type_enum
        if self.crf_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.crf_type_enum, "IEEE1722TpCrfTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRF-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize frame_sync
        if self.frame_sync is not None:
            serialized = SerializationHelper.serialize_item(self.frame_sync, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp
        if self.timestamp is not None:
            serialized = SerializationHelper.serialize_item(self.timestamp, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMESTAMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpCrfConnection":
        """Deserialize XML element to IEEE1722TpCrfConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpCrfConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpCrfConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-FREQUENCY":
                setattr(obj, "base_frequency", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "CRF-PULL-ENUM":
                setattr(obj, "crf_pull_enum", IEEE1722TpCrfPullEnum.deserialize(child))
            elif tag == "CRF-TYPE-ENUM":
                setattr(obj, "crf_type_enum", IEEE1722TpCrfTypeEnum.deserialize(child))
            elif tag == "FRAME-SYNC":
                setattr(obj, "frame_sync", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TIMESTAMP":
                setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class IEEE1722TpCrfConnectionBuilder(IEEE1722TpAvConnectionBuilder):
    """Builder for IEEE1722TpCrfConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpCrfConnection = IEEE1722TpCrfConnection()


    def with_base_frequency(self, value: Optional[PositiveInteger]) -> "IEEE1722TpCrfConnectionBuilder":
        """Set base_frequency attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base_frequency' is required and cannot be None")
        self._obj.base_frequency = value
        return self

    def with_crf_pull_enum(self, value: Optional[IEEE1722TpCrfPullEnum]) -> "IEEE1722TpCrfConnectionBuilder":
        """Set crf_pull_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'crf_pull_enum' is required and cannot be None")
        self._obj.crf_pull_enum = value
        return self

    def with_crf_type_enum(self, value: Optional[IEEE1722TpCrfTypeEnum]) -> "IEEE1722TpCrfConnectionBuilder":
        """Set crf_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'crf_type_enum' is required and cannot be None")
        self._obj.crf_type_enum = value
        return self

    def with_frame_sync(self, value: Optional[Boolean]) -> "IEEE1722TpCrfConnectionBuilder":
        """Set frame_sync attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'frame_sync' is required and cannot be None")
        self._obj.frame_sync = value
        return self

    def with_timestamp(self, value: Optional[PositiveInteger]) -> "IEEE1722TpCrfConnectionBuilder":
        """Set timestamp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'timestamp' is required and cannot be None")
        self._obj.timestamp = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "baseFrequency",
        "crfPullEnum",
        "crfTypeEnum",
        "frameSync",
        "timestamp",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IEEE1722TpCrfConnection:
        """Build and return the IEEE1722TpCrfConnection instance with validation."""
        self._validate_instance()
        return self._obj