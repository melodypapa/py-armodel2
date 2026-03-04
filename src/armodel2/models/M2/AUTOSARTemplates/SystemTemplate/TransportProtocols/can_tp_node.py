"""CanTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 611)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CanTpNode(Identifiable):
    """AUTOSAR CanTpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CAN-TP-NODE"


    connector_ref: Optional[Any]
    max_fc_wait: Optional[Integer]
    st_min: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    tp_address_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONNECTOR-REF": lambda obj, elem: setattr(obj, "connector_ref", ARRef.deserialize(elem)),
        "MAX-FC-WAIT": lambda obj, elem: setattr(obj, "max_fc_wait", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "ST-MIN": lambda obj, elem: setattr(obj, "st_min", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-AR": lambda obj, elem: setattr(obj, "timeout_ar", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-AS": lambda obj, elem: setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TP-ADDRESS-REF": lambda obj, elem: setattr(obj, "tp_address_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize CanTpNode."""
        super().__init__()
        self.connector_ref: Optional[Any] = None
        self.max_fc_wait: Optional[Integer] = None
        self.st_min: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.tp_address_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CanTpNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanTpNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connector_ref
        if self.connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.connector_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_fc_wait
        if self.max_fc_wait is not None:
            serialized = SerializationHelper.serialize_item(self.max_fc_wait, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-FC-WAIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize st_min
        if self.st_min is not None:
            serialized = SerializationHelper.serialize_item(self.st_min, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ST-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_ar
        if self.timeout_ar is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_ar, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_as
        if self.timeout_as is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_as, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_address_ref
        if self.tp_address_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_address_ref, "CanTpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-ADDRESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpNode":
        """Deserialize XML element to CanTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanTpNode, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONNECTOR-REF":
                setattr(obj, "connector_ref", ARRef.deserialize(child))
            elif tag == "MAX-FC-WAIT":
                setattr(obj, "max_fc_wait", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "ST-MIN":
                setattr(obj, "st_min", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-AR":
                setattr(obj, "timeout_ar", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-AS":
                setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TP-ADDRESS-REF":
                setattr(obj, "tp_address_ref", ARRef.deserialize(child))

        return obj



class CanTpNodeBuilder(IdentifiableBuilder):
    """Builder for CanTpNode with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CanTpNode = CanTpNode()


    def with_connector(self, value: Optional[any (Communication)]) -> "CanTpNodeBuilder":
        """Set connector attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.connector = value
        return self

    def with_max_fc_wait(self, value: Optional[Integer]) -> "CanTpNodeBuilder":
        """Set max_fc_wait attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_fc_wait = value
        return self

    def with_st_min(self, value: Optional[TimeValue]) -> "CanTpNodeBuilder":
        """Set st_min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.st_min = value
        return self

    def with_timeout_ar(self, value: Optional[TimeValue]) -> "CanTpNodeBuilder":
        """Set timeout_ar attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_ar = value
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> "CanTpNodeBuilder":
        """Set timeout_as attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_as = value
        return self

    def with_tp_address(self, value: Optional[CanTpAddress]) -> "CanTpNodeBuilder":
        """Set tp_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_address = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "connector",
        "maxFcWait",
        "stMin",
        "timeoutAr",
        "timeoutAs",
        "tpAddress",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CanTpNode:
        """Build and return the CanTpNode instance with validation."""
        self._validate_instance()
        return self._obj